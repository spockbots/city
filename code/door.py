
#! /usr/bin/env micropython

import spockbots.robot as robot
from time import sleep

def medium_left(speed, degrees):
    robot.mediummotor_left.on_for_rotations(speed, int(degrees/360))

medium_left(25, 10)


robot.mediummotor_left.on_for_rotations(-25, int(10/360))