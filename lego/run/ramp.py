#!/usr/bin/env pybricks-micropython

from spockbots.motor import SpockbotsMotor
from spockbots.gyro import SpockbotsGyro as Gyro
from time import sleep
from spockbots.output import led, PRINT

def run_ramp():
    """
    TBD
    """
    robot = SpockbotsMotor()
    robot.debug = True

    robot.setup(direction="backwards")
    robot.colorsensors.read()

    print(robot)

    #
    # setup gyro
    #
    gyro = Gyro(robot)
    gyro.setup()


    robot.forward(50,80)
    robot.turn(25,15)
    robot.gotowhite(10,4)
    robot.forward(10,10)


    gyro.turn(10, 75)

    robot.followline(speed=10, distance=15, port=4, right=False, delta=-35, factor=0.4)
    robot.forward(75,80)

    #
    # stall the robot
    #
    while True:
        pass


if __name__ == "__main__":
    run_ramp()
