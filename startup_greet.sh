#!/bin/bash

JCONF=~/julius/dictation-kit-4.5/am-gmm.jconf
DICT=~/julius/dict/greet

echo JCONF=$JCONF
echo DICT=$DICT

CMD="julius -C $JCONF -nostrip -gram $DICT -input mic -module"
echo $CMD
$CMD
