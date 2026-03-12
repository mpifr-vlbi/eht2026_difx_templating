#!/bin/bash

tracklist=`grep TRACKS_230G ../Makefile.inc | sed "s/TRACKS_230G := //g"`
stations="Aa Ax Gl Pv Lm Kt Mg Mm Sw Sz Ky Pc"

function makeBonnDatadir() {
	cmd="mkdir /data/"$1
	sg evlbi -c "$cmd"
	chmod g+sw /data/$1
	chmod o-rwx /data/$1
	chown oper:evlbi /data/$1
}

# Bonn
if true; then
	for track in ${tracklist}; do
		for station in ${stations}; do
			makeBonnDatadir ${track}
			makeBonnDatadir ${track}/${station}
			for band in b1 b2 b3 b4; do
				makeBonnDatadir ${track}/${station}/${band}/
				makeBonnDatadir ${track}/${station}/${band}/12
				makeBonnDatadir ${track}/${station}/${band}/34
				makeBonnDatadir ${track}/${station}/${band}/s12
				makeBonnDatadir ${track}/${station}/${band}/s34
			done
		done
		# Special case: NOEMA
		station=Nn
		makeBonnDatadir ${track}/${station}
		for band in b1 b2 b3 b4; do
			makeBonnDatadir ${track}/${station}/${band}/
			for slot in 1 2 3 4; do
				makeBonnDatadir ${track}/${station}/${band}/${slot}/
				makeBonnDatadir ${track}/${station}/${band}/s${slot}/
			done
		done
	done
fi

# Haystack
# Possibly like this pattern,
#   /data-st52/eht/<expt>/<2-letter station code>/b2/s12/ - band 2, recorder slots 1&2
#   /data-st52/eht/<expt>/<2-letter station code>/b2/s34/ - band 2, recorder slots 3&4
#   /data-st52/eht/<expt>/<2-letter station code>/b2/s12/ - band 3, recorder slots 1&2
#   /data-st52/eht/<expt>/<2-letter station code>/b2/s34/ - band 3, recorder slots 3&4
if false; then
	echo todo
fi

