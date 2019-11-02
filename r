#! /bin/sh

ROBOT=robot@ev3dev.local

scp -r code/spockbots code/*.py $ROBOT:.

#scp -r code/spockbots code/*.py yellow:.
#scp -r code/spockbots code/*.py robot:.

#scp -r code/wav code/*.py robot@ev3dev.local:.



#scp -r code/spockbots code/*.py robot@ev3dev.local:.
#ssh robot@ev3dev.local "micropython ./check.py"

#PRG="color"
#PRG="main"
#PRG="diff" # interpreter must by python3
#PRG="line"
#PRG="sound"
#PRG="check"
#PRG="gyro"
#PRG="interpreter"
#PRG="line_sample"
#PRG="calibrate"

PRG=$1

scp -r code/$PRG.py $ROBOT:.

ssh $ROBOT "micropython ./$PRG.py"
#ssh robot@ev3dev.local "python3 ./$PRG.py"


