#! /bin/sh
# rsync -e ssh . robot@ev3dev.local:.
scp -r spockbots *.py robot@ev3dev.local:.
ssh robot@ev3dev.local "micropython ./main.py"

