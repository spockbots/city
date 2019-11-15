#!/usr/bin/env pybricks-micropython

from spockbots.gyro import SpockbotsGyro as Gyro
from spockbots.motor import SpockbotsMotor
import time


def run_crane():
    """
    lower the block from the crane
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

    robot.forward(50, 20)

    robot.gotowhite(25, 3)
    robot.turntoblack(25, direction="right", port=3)

    robot.forward(50, 5)

    robot.turntowhite(15, direction="left", port=2)

    robot.followline(speed=10, distance=13,
                     port=2, right=True,
                     delta=-35, factor=0.4)

    robot.forward(50, -5)

    robot.gotowhite(10, 3)
    robot.gotoblack(10, 3)
    robot.gotowhite(10, 3)

    robot.forward(2, 4)
    robot.forward(10, 1)

    # back to base

    robot.forward(5, -5)  # backup slowly
    robot.forward(100, -20)
    robot.turn(25, 56)
    robot.forward(100, -60)


if __name__ == "__main__":
    time_start = time.time()
    run_crane()
    time_end = time.time()
    print("Time:", time_end - time_start)

    # Time: 27.17