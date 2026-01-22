#!/bin/bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
OUTDIR=../templates/common_sections/

pushd $SCRIPT_DIR  2>&1 > /dev/null

./geteop.pl 2026-019  5 $OUTDIR/eop_e26j21.vex
# ./geteop.pl 2026-020  5 $OUTDIR/eop_e26j22.vex
# ./geteop.pl 2026-021  5 $OUTDIR/eop_e26j23.vex

popd  2>&1 > /dev/null

