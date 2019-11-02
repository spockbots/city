#!/usr/bin/env python3

import spockbots.robot as robot
import sys


robot.beep()
robot.gyro.reset()
robot.read()
robot.colorsensors.info()
robot.direction("front")
robot.beep()



#robot.followline(speed=10, t=3, port=3, black=15, white=80, delta=-35, factor = 0.4)
robot.followline(distance=50, port=3, speed=25, black=20, white=80, delta=-35, factor=0.28)
#robot.followline(speed=25, distance=10, port=3, delta=-30, factor=0.5)
