#!/usr/bin/env pybricks-micropython

from spockbots.motor import SpockbotsMotor
from spockbots.gyro import SpockbotsGyro as Gyro
from time import sleep
from spockbots.output import led, PRINT

def run_tan_circle():
    """
    TBD
    """
    robot = SpockbotsMotor()
    robot.debug = True

    robot.setup()
    robot.color.read()

    print(robot)

    #
    # setup gyro
    #
    gyro = Gyro(robot)
    gyro.setup()

    # move a long distance
    robot.forward(30,85)
    # trun towards the white line
    robot.turn(25,-45)
    # move a bit forward so we are not in the red circle as it colld be interpreted as white
    robot.forward(25,23)

    # back up and leave the building
    robot.forward(25,-15)
    # turn to home
    robot.turn(25, 15)
    # go back to base
    robot.forward(100, -100)

if __name__ == "__main__":
    run_tan_circle()
