#!/usr/bin/env python3

import spockbots.robot as robot
import time


robot.gyro.reset()

while True:
    angle = robot.gyro.angle()
    print("Run Angle: ", angle)