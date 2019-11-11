#!/usr/bin/env pybricks-micropython

from spockbots.motor import SpockbotsMotor
from time import sleep


def run_black_circle():
    """
    TBD
    """
    robot = SpockbotsMotor()
    robot.debug = True

    robot.setup()
    robot.color.read()

    print(robot)

    robot.forward(30,48)
    robot.forward(10,-15)
    robot.forward(50, -30)


if __name__ == "__main__":
    run_black_circle()

