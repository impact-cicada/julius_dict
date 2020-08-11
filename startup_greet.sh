#!/bin/bash

JCONF=~/julius/grammar-kit-4.3.1/hmm_mono.jconf
DICT=~/julius/dict/greet
LEVEL=5000
RJSH=600

echo JCONF=$JCONF
echo DICT=$DICT

CMD="julius -C $JCONF -nostrip -gram $DICT -lv $LEVEL -rejectshort $RJSH -input mic -module"
echo $CMD
$CMD
