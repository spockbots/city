#!/usr/bin/env python3

import spockbots.robot as robot
import sys

robot.beep()
robot.gyro.reset()
robot.read()
robot.colorsensors.info()
robot.beep()


def crane():
    robot.forward(50, 60)
    robot.door_open()
    robot.forward(-8, 15)
    robot.forward(-100, 60)

crane()