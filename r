#! /bin/sh

scp -r code/spockbots code/*.py robot@ev3dev.local:.

#scp -r code/wav code/*.py robot@ev3dev.local:.



#scp -r code/spockbots code/*.py robot@ev3dev.local:.
#ssh robot@ev3dev.local "micropython ./check.py"

#PRG="color"
#PRG="main"
#PRG="diff" # interpreter must by python3
#PRG="line"
#PRG="sound"
#PRG="check"
PRG="gyro"


#scp -r code/$PRG.py robot@ev3dev.local:.

ssh robot@ev3dev.local "micropython ./$PRG.py"
#ssh robot@ev3dev.local "python3 ./$PRG.py"


