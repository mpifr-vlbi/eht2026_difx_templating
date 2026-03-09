#!/bin/bash

tracklist=`grep TRACKS_230G ../Makefile.inc | sed "s/TRACKS_230G := //g"`

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
		makeBonnDatadir ${track}
		makeBonnDatadir ${track}/b1/
		makeBonnDatadir ${track}/b2/
		makeBonnDatadir ${track}/b3/
		makeBonnDatadir ${track}/b4/
		makeBonnDatadir ${track}/b1/12/
		makeBonnDatadir ${track}/b1/34/
		makeBonnDatadir ${track}/b2/12/
		makeBonnDatadir ${track}/b2/34/
		makeBonnDatadir ${track}/b3/12/
		makeBonnDatadir ${track}/b3/34/
		makeBonnDatadir ${track}/b4/12/
		makeBonnDatadir ${track}/b4/34/
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

