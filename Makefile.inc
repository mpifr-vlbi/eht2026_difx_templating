# Which tracks to generate
# removed e26j21
TRACKS_230G := e26m10 e26m13 e26m17 e26m20 e26m24 e26m27 e26m31 e26a03 e26a07 e26a10 e26a14 e26a17 e26a21 e26a24 e26a28
TRACKS_345G :=

# Revision of correlation run, e.g., v1a, gold253, gold261, gold262
#REV  := v1
REV := FRINGE

# Release version, e.g., 1 as in e22d23-1-b1
REL  := 0

# Name of site; used for ./filelists_<SITE>/
SITE := mpifr

# Top-level directory for Correlator output, any experiment
# The generated files <trackname>-$REL-{b1,b2,b3,b4}.{v2d,vex.obs}
# will be placed under directories $EXPROOT/<trackname>/$REV/<band>/
EXPROOT := /Exps/
