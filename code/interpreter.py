#!/usr/bin/env python

import spockbots.robot as robot
import sys

while True:
    line = input("spockbots >>> ")
    if line == "q":
        print ("quit")
        sys.exit()
    try:
        eval(line)
    except Exception as e:
        print()
        print(e)
        print()