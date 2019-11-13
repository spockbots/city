#!/usr/bin/env pybricks-micropython
from spockbots.motor import SpockbotsMotor
import time

# from spockbots.systemgyro import Gyro
from spockbots.gyro import SpockbotsGyro as Gyro
from spockbots.output import led, PRINT
import sys
import os

robot = SpockbotsMotor()
robot.setup()

robot.color.read()
print(robot)

gyro = Gyro(robot)
gyro.setup()

# from importlib import reload

robot.setup()

while True:
    line = input("spockbots >>> ")
    if line == "q":
        print("quit")
        sys.exit()
    elif line.startswith("gyro.") or \
            line.startswith("robot.") or \
                line.startswith("run."):
        try:
            print(line)
            eval(line)
        except Exception as e:
            print()
            print(e)
            print()
    elif line == "s":
        os.system("./stop.py")
    elif line.startswith("p "):
        try:
            line = line[2:]
            print(line)
            eval("print (robot." + line + ")")
        except Exception as e:
            print()
            print(e)
            print()
    elif line == "r":
        try:
            print("Reloading ....")
            # x = reload(robot)
            # print(x)
            robot.beep()
            # robot.gyro.reset()
            # robot.read()
            # robot.colorsensors.info()
            # robot.beep()
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
