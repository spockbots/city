#!/usr/bin/env pybricks-micropython

from spockbots.motor import SpockbotsMotor
import time


def run_turn_to_black():
    """
    TBD
    """
    robot = SpockbotsMotor()
    robot.debug = True
    robot.setup()
    robot.colorsensors.read()

    print(robot)

    robot.beep()

    """
    robot.tunrtoblack(5,
                      direction="right",
                      port=3,
                      black=10)
    """

    robot.tunrtoblack(5,
                      direction="left",
                      port=2,
                      black=10)

    robot.beep()

    time.sleep(1)


if __name__ == "__main__":
    run_turn_to_black()
