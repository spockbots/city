#!/usr/bin/env pybricks-micropython
from spockbots.motor import SpockbotsMotor
import time

def run_swing():
    """
    TBD
    """
    robot = SpockbotsMotor()
    robot.debug = True

    robot.setup()

    robot.color.read()
    print(robot)

    import sys
    import os

    # from importlib import reload

    robot.setup()

    # PUT IN COLOR CALIBRATE VALUES

    robot.forward(20, 30)

    robot.turn(50, -20)  # just robot: -5  just attachment: -20 speed 50  attachment with blocks: ??

    robot.followline(speed=10,
                     distance=72,
                     port=3,
                     right=True,
                     black=15,
                     white=85,
                     delta=-35,
                     factor=0.4)
    # for some reason right=True is left side of line

    robot.turn(50, 55)  # just robot: 20  just attachment: 55 speed 50  attachment with blocks: ??
    # for sr positive angle turns left

    robot.followline(speed=10,
                     distance=43,
                     port=3,
                     right=True,
                     black=15,
                     white=85,
                     delta=-35,
                     factor=0.4)
