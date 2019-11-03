#! /usr/bin/env pybricks-micropytho

from spockbots.motor import SpockbotsMotor
import time

robot = SpockbotsMotor()
robot.setup()

print(robot)

def door_motor(speed, degrees):
    robot.left_medium.on_for_rotations(speed, int(degrees/360))



door_motor(25, 10)


robot.mediummotor_left.on_for_rotations(-25, int(10/360))