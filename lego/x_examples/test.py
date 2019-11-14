#!/usr/bin/env pybricks-micropython
from spockbots.motor import SpockbotsMotor
import time

robot = SpockbotsMotor()
robot.setup()

print(str(robot))

robot.beep()
robot.calibrate(10,
                distance=30,
                ports=[2, 3, 4],
                direction='front')
robot.beep()

# robot.forward(25,10)

# robot.calibrate(10, ports=[4], direction='back')

robot.colorsensors.write()

time.sleep(1)
