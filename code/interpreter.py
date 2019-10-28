#!/usr/bin/env python3

import spockbots.robot as robot
import sys

robot.beep()
robot.gyro.reset()
robot.read()
robot.colorsensors.info()
robot.beep()


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