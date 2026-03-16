# eht2026_difx_templating
EHT 2026 VLBI DiFX correlation setups


# Dress Rehearsal 2026

GLT used the nominal EHT 230G setup with a 1st LO of 221.100 GHz and 2nd LO of 7.000 GHz (both exact, no LO offsets).


# Monitoring Campaign 2026

Fringe checks done weekly during the campaign are intended to build the necessary DiFX setups
to enable rapid production correlation right at the end of the campaign, after shipped modules arrive.

Fringe checks are kept track of under https://eventhorizontelescope.mywikis.wiki/wiki/Observing/2026_Movie_Campaign/Correlation#Completed_Fringe_Checks

## e26m10

LMT is band-swapped in e26m10 e26m13, b1<->2 for sure, and possibly but not verified b3<->b4.

Pico worked on the DR e26j21 rate 'sidelobe' issue. Appears resolved in e26m10. After e26m10,
Pico also fixed a power splitter in their H-maser. Fringes in e26m13 on Nn-Pv look excellent.

NOEMA pad probably alway N020, H-maser rate practically 0.0e-12

APEX in e26m10 had inadvertently 2:1 sample decimation, producing aliased an 1024 MHz
bandwidth (instead of the nominal bw of 2048 MHz as in later tracks). In b2 VEX a
chan_def setting of 214100.0 MHz : U :1024.00 MHz for APEX produced fringes. ToDo is
checking b1 b3 b4 and adding this e26m10 Ax chan_def exception into the templates.

## e26m13

So far all-nominal.


