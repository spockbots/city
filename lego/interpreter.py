#!/usr/bin/env pybricks-micropython
from spockbots.motor import SpockbotsMotor
import time

robot = SpockbotsMotor()
robot.setup()

robot.color.read()
print(robot)


import sys
import os
# from importlib import reload

robot.setup()

while True:
    line = input("spockbots >>> ")
    if line == "q":
        print ("quit")
        sys.exit()
    elif line == "s":
        os.system("./stop.py")
    elif line.startswith("p "):
        try:
            line = line[2:]
            print (line)
            eval("print (robot." + line + ")")
        except Exception as e:
            print()
            print(e)
            print()
    elif line == "r":
        try:
            print("Reloading ....")
            #x = reload(robot)
            #print(x)
            robot.beep()
            #robot.gyro.reset()
            #robot.read()
            #robot.colorsensors.info()
            #robot.beep()
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