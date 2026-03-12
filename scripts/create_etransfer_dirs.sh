#!/bin/bash

tracklist=`grep TRACKS_230G ../Makefile.inc | sed "s/TRACKS_230G := //g"`
stations="Aa Ax Gl Nn Pv Lm Kt Mg Mm Sw Sz Ky Pc"

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
			makeBonnDatadir ${track}/${station}/b1/
			makeBonnDatadir ${track}/${station}/b2/
			makeBonnDatadir ${track}/${station}/b3/
			makeBonnDatadir ${track}/${station}/b4/
			makeBonnDatadir ${track}/${station}/b1/12/
			makeBonnDatadir ${track}/${station}/b1/34/
			makeBonnDatadir ${track}/${station}/b2/12/
			makeBonnDatadir ${track}/${station}/b2/34/
			makeBonnDatadir ${track}/${station}/b3/12/
			makeBonnDatadir ${track}/${station}/b3/34/
			makeBonnDatadir ${track}/${station}/b4/12/
			makeBonnDatadir ${track}/${station}/b4/34/
			makeBonnDatadir ${track}/${station}/b1/s12/
			makeBonnDatadir ${track}/${station}/b1/s34/
			makeBonnDatadir ${track}/${station}/b2/s12/
			makeBonnDatadir ${track}/${station}/b2/s34/
			makeBonnDatadir ${track}/${station}/b3/s12/
			makeBonnDatadir ${track}/${station}/b3/s34/
			makeBonnDatadir ${track}/${station}/b4/s12/
			makeBonnDatadir ${track}/${station}/b4/s34/
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

