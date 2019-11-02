#! /bin/sh

ROBOT=$1
PRG=$2

PYTHON="python3"
# PYTHON="micropython"

echo
echo "Uploading files"
echo

scp -r code/spockbots code/*.py $ROBOT:.

echo
echo "Starting $PRG"
echo
ssh $ROBOT "$PYTHON ./$PRG.py"


