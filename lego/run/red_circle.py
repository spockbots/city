#!/usr/bin/env pybricks-micropython

from spockbots.motor import SpockbotsMotor
from spockbots.gyro import SpockbotsGyro as Gyro
import time
from spockbots.output import led, PRINT


def run_red_circle():
    """
    Drive the red peces in the red circle
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

    # run forward
    gyro.forward(25, 59)
    # turn to red circle
    gyro.turn(10, -40)
    # move it a bit more in
    gyro.forward(10, 3)
    # back up
    robot.forward(10, -10)
    # turn to base
    gyro.turn(10, 45)
    # got to base
    robot.forward(75, -70)

if __name__ == "__main__":
    time_start = time.time()
    run_red_circle()
    time_end = time.time()
    print("Time:", time_end - time_start)

    # Time: 17.00
