#!/usr/bin/python3
from __future__ import print_function
import requests
import datetime
import pytz

server = 'vlbimon1'
SERVER = 'https://%s.science.ru.nl' % server
FNAME = '.sessionid.%s.txt' % server

def get_session():
    '''Setup user session with server'''
    def restore_session(s):
        #-- read from file
        with open(FNAME, 'r') as f:
            sessionid = f.readline().strip()
        #-- validate
        s.cookies.set('sessionid', sessionid)
        url = SERVER + '/session/' + sessionid
        r = s.patch(url)
        r.raise_for_status()
        return s
        
    def create_session(s):
        url = SERVER + '/session'
        import getpass
        username = input('Username:')
        password = getpass.getpass('Password for {:}:'.format(username))
        r = s.post(url, auth=requests.auth.HTTPBasicAuth(username, password))
        r.raise_for_status()
        resp = r.json()
        sessionid = resp['id']
        s.cookies.set('sessionid', sessionid)
        #-- write to file
        with open(FNAME, 'w') as f:
            f.write(sessionid)
        return s

    s = requests.Session()
    #-- restore session
    try:
        return restore_session(s)
    except: pass
    #-- create new session if restore failed
    return create_session(s)

def fetch_timeseries(s, timebracket, sites=[], fields=[]):
    '''Fetch metadata timeseries data from server'''
    url = SERVER + '/data/history'

    tail = ['observatory=' + s for s in sites]
    tail += ['field=' + f for f in fields]
    tail += ['startTime=%d' % timebracket[0], 'endTime=%d' % timebracket[1]]
    if len(tail) > 0:
        url += '?' + '&'.join(tail)

    r = s.get(url)
    r.raise_for_status()
    return r.json()

if __name__ == '__main__':
    from argparse import ArgumentParser
    import numpy as np
    from scipy.stats import linregress
    import matplotlib.pyplot as plt

    default_sites = ['GLT','JCMT','KP','LMT','SMA','SMT','SPT']
    default_bands = [1,2,3,4]
    rate_units = ['s/s','ms/s','us/s','ns/s','ps/s','fs/s']
    offset_units = ['s','ms','us','ns','ps','fs']
    ap = ArgumentParser()
    ap.add_argument('--sites', nargs='+', metavar='SITE', help='limit to these sites (default={})'.format(' '.join(default_sites)), default=default_sites)
    ap.add_argument('--bands', nargs='+', metavar='BANDNUM', help='limit to given band numbers (default={})'.format(' '.join(['{}'.format(b) for b in default_bands])), default=default_bands, type=int)
    ap.add_argument('--rate-unit', metavar='UNIT', help='rate in UNIT, one of {} (default=ps/s)'.format(rate_units), default='ps/s', choices=rate_units)
    ap.add_argument('--offset-unit', metavar='UNIT', help='offset in UNIT, one of {} (default=ns)'.format(offset_units), default='ns', choices=offset_units)
    ap.add_argument('--start-time', metavar='START', help='limit to data after START, format %%Yy%%jd%%Hh%%Mm%%Ss (default is last R2DBE configure time)', type=lambda s: datetime.datetime.strptime(s, '%Yy%jd%Hh%Mm%Ss').replace(tzinfo=pytz.UTC))
    ap.add_argument('--stop-time', metavar='STOP', help='limit to data before STOP, format %%Yy%%jd%%Hh%%Mm%%Ss (default is now)', type=lambda s: datetime.datetime.strptime(s, '%Yy%jd%Hh%Mm%Ss').replace(tzinfo=pytz.UTC))
    ap.add_argument('--make-vex', metavar='FILE', help='output clock information to FILE, always in append mode')
    args = ap.parse_args()

    # gather arguments
    sites = args.sites
    bands = sorted(args.bands)
    rate_unit = args.rate_unit
    rate_div = dict(zip(rate_units,[10**(-x) for x in [0,3,6,9,12,15]]))[rate_unit]
    offset_unit = args.offset_unit
    offset_div = dict(zip(offset_units,[10**(-x) for x in [0,3,6,9,12,15]]))[offset_unit]
    start_time = args.start_time
    stop_time = args.stop_time
    vex_file = args.make_vex

    r2dbes = [1,2,3,4]
    fpga_clk = 256e6
    t0,tnow = [(datetime.datetime.utcnow() - datetime.timedelta(days=d)).timestamp() for d in [365*1,0]]

    # set up session with vlbimon server
    ses = get_session()

    # process separately for each r2dbe for each site
    for site in sites:
        print(site)
        plt.figure(site)
        # count number of datasets per site
        count = 0
        for r2 in r2dbes:
            # get band information
            bandnum = 0
            for ch in [0,1]:
                sideband = 'r2dbe_{}_rxSideband{}'.format(r2,ch)
                bdcband = 'r2dbe_{}_bdcBand{}'.format(r2,ch)
                result = fetch_timeseries(ses, [t0, tnow], [site], [sideband, bdcband])
                try: bandstr = '_'.join([result[site][x.format(r2,ch)][-1][-1] for x in [sideband, bdcband]])
                except (KeyError,IndexError) as e: continue
                try: bandnum = {'lsb_high':1,'lsb_low':2,'usb_low':3,'usb_high':4}[bandstr]
                except (KeyError) as e: continue
            if bandnum not in bands: continue

            # initialize plots
            ax1 = plt.subplot(2,len(bands),bands.index(bandnum)+1)
            if r2 == 1: plt.ylabel('ToA of GPS 1PPS after R2DBE internal 1PPS [{}]'.format(offset_unit))
            ax2 = plt.subplot(2,len(bands),bands.index(bandnum)+1+len(bands))
            if r2 == 1: plt.ylabel('Residual after fit [{}]'.format(offset_unit))

            # get upSince time first
            upsince = 'r2dbe_{}_upSince'.format(r2)
            result = fetch_timeseries(ses, [t0, tnow], [site], [upsince])
            try: t1 = result[site][upsince][-1][-1]
            except (KeyError,IndexError) as e: continue
            tup,r2up = [[u[i] for u in result[site][upsince]] for i in [0,1]]

            # now get ppsOffset logged since upSince
            ppsoffset = 'r2dbe_{}_ppsOffset'.format(r2)
            tstart = t1 if start_time is None else start_time.timestamp()
            tstop = tnow if stop_time is None else stop_time.timestamp()
            if tstop > tnow:
                print('    (stop time limited to now)')
                tstop = tnow
            if tstart >= tstop:
                print('    (stop time before start time, reverting to defaults)')
                tstart,tstop = t1,tnow
            # check if there are any r2dbe configs in the window
            r2break = []
            r2break_last = None
            for u in r2up:
                if u > tstart and u < tstop:
                    # handle upSince jitter of less than 10 seconds
                    if r2break_last is not None and len(r2break) > 0:
                        if abs(r2break_last-u) < 10:
                            continue
                    r2break.append(u)
                    r2break_last = u
            if len(r2break) > 0:
                print('    (found %d R2DBE reconfigure(s) in requested time)' % len(r2break))
                r2break = sorted(r2break)
                for i,u in enumerate(r2break):
                    print('        #%3d:   %s   %d' % (i+1, datetime.datetime.fromtimestamp(u,tz=pytz.UTC).strftime('%Yy%jd%Hh%Mm%Ss'), u))
                print('    (limiting window to after reconfigure @ %s)' % datetime.datetime.fromtimestamp(r2break[-1],tz=pytz.UTC).strftime('%Yy%jd%Hh%Mm%Ss'))
                tstart = r2break[-1]
            result = fetch_timeseries(ses, [tstart, tstop], [site], [ppsoffset])
            try: t,r = [np.array(x[1:]) for x in zip(*result[site][ppsoffset])]
            except (KeyError,IndexError) as e: continue

            # increment number of datasets for this site
            count += 1

            # linear fit
            delta = r/fpga_clk
            T = [datetime.datetime.fromtimestamp(tt,tz=pytz.UTC) for tt in t]
            linreg = linregress(t,delta)
            y = np.polyval([linreg.slope,linreg.intercept],t)
            res = y - delta

            # print results
            tstr = datetime.datetime.fromtimestamp(t[0],tz=pytz.UTC).strftime('%Yy%jd%Hh%Mm%Ss')
            print('  band {}: rate = {:+.3f} +/- {:.3f} {}, offset = {:+.3f} {} @ {} [{} pts]'.format(bandnum,linreg.slope/rate_div,linreg.stderr/rate_div,rate_unit,y[0]/offset_div,offset_unit,tstr,len(t)))

            # plot data & fit
            plt.sca(ax1)
            plt.plot(T,delta/offset_div,'o',label='data')
            plt.plot(T,y/offset_div,'--',label='linear fit')
            plt.title('band {}: rate = {:+.3f} {}'.format(bandnum, linreg.slope/rate_div, rate_unit))
            plt.xlabel('Time')
            plt.xticks(rotation=40)
            #plt.xticks(ticks=[T[0],T[-1]])
            plt.grid()

            # plot residual
            plt.sca(ax2)
            plt.plot(T,res/offset_div)
            plt.xlabel('Time')
            plt.xticks(rotation=40)
            #plt.xticks(ticks=[T[0],T[-1]])
            plt.grid()

            # write to file if requested
            if vex_file is None: continue
            vex_out = 'def {}_band{};\n'.format(site,bandnum)
            vex_out += '  clock_early = {} : {:.3f} usec : {} : {:.3f} psec/sec;\n'.format(T[0].strftime('%Yy%jd%Hh%Mm%Ss'), y[0]/1e-6, T[0].strftime('%Yy%jd%Hh%Mm%Ss'), linreg.slope/1e-12)
            vex_out += 'enddef;\n'
            with open(vex_file, 'a') as fh:
                fh.write(vex_out)

        # if no data for site, close the plot
        if count == 0:
            plt.close()
            print('    (no data for site)')
        else:
            # save plot
            figname = 'clock_' + site + '_bands' + ''.join(['{}'.format(b) for b in bands]) + '.png'
            w,h = plt.gcf().get_size_inches()
            plt.gcf().set_size_inches([3*w,1.5*h])
            plt.tight_layout()
            plt.savefig(figname,dpi=plt.gcf().dpi*4)
            print('  (saved plot {})'.format(figname))

        if vex_file is not None: print('  (wrote clock to file {})'.format(vex_file))

    plt.show()
