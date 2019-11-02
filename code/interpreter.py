#!/usr/bin/env python3

import spockbots.robot as robot
import sys
import os
from importlib import reload

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
    elif line == "s":
        os.system("./stop.py")
    elif line == "r":
        try:
            print("Reloading ....")
            x = reload(robot)
            print(x)
            robot.beep()
            robot.gyro.reset()
            robot.read()
            robot.colorsensors.info()
            robot.beep()
        except Exception as e:
            print()
            print(e)
            print()
    else:
        try:
            eval("robot." + line)
        except Exception as e:
            print()
            print(e)
            print()