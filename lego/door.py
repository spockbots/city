#! /usr/bin/env pybricks-micropython

from spockbots.motor import SpockbotsMotor
import time

robot = SpockbotsMotor()
robot.setup()

print(robot)


def door_motor(speed, degrees):
    robot.left_medium.run_angle(speed * 25, degrees)


door_motor(25, 360)

# robot.mediummotor_left.on_for_rotations(-25, 10/360)

time.sleep(1)
