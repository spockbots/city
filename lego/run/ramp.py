#!/usr/bin/env pybricks-micropython

from spockbots.motor import SpockbotsMotor
from spockbots.gyro import SpockbotsGyro as Gyro
from spockbots.output import led, PRINT
import time


def run_ramp():
    """
    Drive up the ramp
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

    # move towards the black line
    gyro.forward(50, 72)
    # go with the robot towards the white  line
    robot.gotowhite(10, 4)
    # Turn so we are allinged with the black line
    gyro.turn(10, 20)
    # Go over the line
    gyro.forward(10, 12)

    # turn to the ramp
    gyro.turn(10, 85)

    # move back
    robot.forward(10, -15)

    # find the line
    robot.turntoblack(10, direction="right", port=4)
    robot.turntowhite(10, direction="left", port=4)

    # follow the line
    robot.followline(speed=10, distance=25, port=4, right=False, delta=-35, factor=0.4)
    # go up the ramp
    gyro.forward(75, 80, min_speed=25, acceleration=10)
    # stop
    robot.stop()

    #
    # stall the robot
    #
    while True:
        pass


if __name__ == "__main__":
    time_start = time.time()
    run_ramp()
    time_end = time.time()
    print("Time:", time_end - time_start)
