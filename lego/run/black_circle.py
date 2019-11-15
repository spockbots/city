#!/usr/bin/env pybricks-micropython

from spockbots.motor import SpockbotsMotor
from time import sleep
from spockbots.gyro import SpockbotsGyro as Gyro
import time


def run_black_circle():
    """
    Drive the white building in the black circle
    """
    robot = SpockbotsMotor()
    robot.debug = True

    robot.setup()
    robot.colorsensors.read()
    print(robot)

    #
    # setup gyro
    #
    gyro = Gyro(robot)
    gyro.setup()

    gyro.forward(30, 48)

    #
    # does not need to be that accurate just bo back
    #
    robot.forward(10, -15)
    robot.forward(50, -30)


if __name__ == "__main__":
    time_start = time.time()
    run_black_circle()
    time_end = time.time()
    print("Time:", time_end - time_start)
