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

./geteop.pl 2026-091  5 $OUTDIR/eop_e26a03.vex  # e26a03.vex: year, doy: 2026,  93
./geteop.pl 2026-095  5 $OUTDIR/eop_e26a07.vex  # e26a07.vex: year, doy: 2026,  97
./geteop.pl 2026-098  5 $OUTDIR/eop_e26a10.vex  # e26a10.vex: year, doy: 2026, 100
./geteop.pl 2026-102  5 $OUTDIR/eop_e26a14.vex  # e26a14.vex: year, doy: 2026, 104
./geteop.pl 2026-105  5 $OUTDIR/eop_e26a17.vex  # e26a17.vex: year, doy: 2026, 107
./geteop.pl 2026-109  5 $OUTDIR/eop_e26a21.vex  # e26a21.vex: year, doy: 2026, 111
./geteop.pl 2026-112  5 $OUTDIR/eop_e26a24.vex  # e26a24.vex: year, doy: 2026, 114
./geteop.pl 2026-116  5 $OUTDIR/eop_e26a28.vex  # e26a28.vex: year, doy: 2026, 118


popd  2>&1 > /dev/null

