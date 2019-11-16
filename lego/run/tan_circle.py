#!/usr/bin/env pybricks-micropython

from spockbots.motor import SpockbotsMotor
from spockbots.gyro import SpockbotsGyro as Gyro
import time
from spockbots.output import led, PRINT


def run_tan_circle():
    """
    Place the tan building in the circle
    """
    robot = SpockbotsMotor()
    robot.debug = True

    robot.setup()
    robot.colorsensors.read()

    print(robot)

    def white():
        return robot.value(2) >= 90
    #
    # setup gyro
    #
    gyro = Gyro(robot)
    gyro.setup()

    #drive to tan circle
    gyro.forward(30, 85)
    gyro.turn(speed=25, degrees=-50, killtime=2)

    #place tan buildings
    gyro.forward(20, 25)

    #back up
    robot.forward(20, -10)

    #turn home
    gyro.turn(speed=25, degrees=50, killtime=2)

    #go home
    robot.forward(100, -120)

if __name__ == "__main__":
    time_start = time.time()
    run_tan_circle()
    time_end = time.time()
    print("Time:", time_end - time_start)

