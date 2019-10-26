#! /bin/sh

scp -r spockbots *.py robot@ev3dev.local:.
#ssh robot@ev3dev.local "micropython ./main.py"

#scp -r code/spockbots code/*.py robot@ev3dev.local:.
#ssh robot@ev3dev.local "micropython ./check.py"

PRG="color"

scp -r code/$PRG.py robot@ev3dev.local:.
ssh robot@ev3dev.local "micropython ./$PRG.py"
