#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
OUTDIR=../templates/common_sections/

pushd $SCRIPT_DIR  2>&1 > /dev/null

./geteop.pl 2026-019  5 $OUTDIR/eop_e26j21.vex

./geteop.pl 2026-067  5 $OUTDIR/eop_e26m10.vex  # e26m10.vex: year, doy: 2026,  69
./geteop.pl 2026-070  5 $OUTDIR/eop_e26m13.vex  # e26m13.vex: year, doy: 2026,  72
./geteop.pl 2026-074  5 $OUTDIR/eop_e26m17.vex  # e26m17.vex: year, doy: 2026,  76
./geteop.pl 2026-077  5 $OUTDIR/eop_e26m20.vex  # e26m20.vex: year, doy: 2026,  79
./geteop.pl 2026-081  5 $OUTDIR/eop_e26m24.vex  # e26m24.vex: year, doy: 2026,  83
./geteop.pl 2026-084  5 $OUTDIR/eop_e26m27.vex  # e26m27.vex: year, doy: 2026,  86
./geteop.pl 2026-088  5 $OUTDIR/eop_e26m31.vex  # e26m31.vex: year, doy: 2026,  90

popd  2>&1 > /dev/null

