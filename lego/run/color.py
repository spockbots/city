#!/usr/bin/env pybricks-micropython
from spockbots.motor import SpockbotsMotor
import time
from spockbots.output import led, PRINT

from spockbots.gyro import SpockbotsGyro as Gyro

from spockbots.output import PRINT

"""GYRO-ANG GYRO-RATE GYRO-FAS GYRO-G&A GYRO-CAL TILT-RATE TILT-ANG"""


def run_color():
    """
    TBD
    """

    robot = SpockbotsMotor()
    robot.debug = True

    robot.setup()
    robot.color.read()

    print(robot)

    while True:
        color = robot.colorsensor.test_color()
        time.sleep(0.1)

if __name__ == "__main__":
    run_color()
