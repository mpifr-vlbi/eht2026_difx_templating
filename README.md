# eht2026_difx_templating
EHT 2026 VLBI DiFX correlation setups


# Dress Rehearsal 2026

GLT used the nominal EHT 230G setup with a 1st LO of 221.100 GHz and 2nd LO of 7.000 GHz (both exact, no LO offsets).


# Monitoring Campaign 2026

Fringe checks done weekly during the campaign are intended to build the necessary DiFX setups
to enable rapid production correlation right at the end of the campaign, after shipped modules arrive.

Fringe checks are kept track of under https://eventhorizontelescope.mywikis.wiki/wiki/Observing/2026_Movie_Campaign/Correlation#Completed_Fringe_Checks

## NOEMA

Reference pad: **N020** in e26m13-e26m17, **N017** in e26m20-e26a03, **N011** in e26a07-e26y05, possibly **N009** in e26y08.

One of the VLBA FPGA output boards was a spare card until and including track e26a14. This spare card had outdated firmware which was missing important fixes.

The outdated firmware partially affected these tracks:
 - e26m13--e26m24: half of b1 RCP; ~1 GHz bw out of 2 pol x 4 band x 2 GHz, possible loss ~6%
 - e26a03--e26a14: part of b1 LCP and entire b2 LCP; ~3 GHz bw out of 16 GHz, possible loss ~19%

The issues are indentical to those [documented for the first GMVA 86 GHz NOEMA fringe test tdec02](https://drive.google.com/drive/folders/1Kog1eLFoCxwty-WXNjihIxywKxVn1yGp):
 - clock offset jumps up to several tens microseconds relative to other cards after a PolyFiX unit is reset
 - small delay offsets in every 4th channel, most visible in HOPS3 fourfit which doesn't fringe fit every channel invidually
 - payload has incorrect 32-bit endianness in the sense of 4 byte groups being internally swapped (BSD be32toh()),
   a fix for proper VDIF files is [swapendianVDIF.c](https://bitbucket.org/jwagner313/kvnvdiftools/src/master/swapendianVDIF.c),
   a fix for Mark6 scatter-gather encapsulated VDIF is ToDo

## APEX

Bands 1 2 and 3 only. The Mark6 for band4 broke in late 2025 and sits in protracted repair at Haystack.

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

No notes so far

## e26m17

SMA/JCMT adjusted their H-maser tuning after e26m17, rate break, tbd

## e26m20

No notes so far

## e26m24

NOEMA issue with Polyfix#1 VLBI card, half the channels in b1 RCP have no fringes. Found out only after seeing the issue in e26a14 b2, during check for rate sidelobes.

Affected NOEMA VLBI card got relocated after the observation into PolyFix#6 in 25th March. The issue (now known at the time) moved together with the card.

## e26m27

Probably NOEMA issue with PolyFix#6 (ex-#1) card; expecting in b2 entire LCP no fringes, b1 half of LCP channels no fringe (cf e26a14)

## e26a03

Probably continued NOEMA b1 b2 LCP issue, just not checked yet

## e26a07

Probably continued NOEMA b1 b2 LCP issue, just not checked yet

## e26a14

Found NOEMA b2 entire LCP pol has no fringes, and in b1 half of the LCP pol channels have no fringes. Their data originate from PolyFix#6.
After e26a14 the affected card might be swapped.

## e26a17

NOEMA other issues (5 MHz distributor), larger part of track failed, only got some low-elevation scans

## e26a21

## e26a24

## e26a28

APEX 1pps distributor box affected by pre-obs power glitch, shifted sync, try DiFX offset +0.893421040 sec (or -0.106578960 sec) as starting point

## e26y08

APEX 1pps distributor box affected by pre-obs power glitch, shifted sync, try DiFX offset +0.169776588 sec (or -0.830223412 sec) as starting point

