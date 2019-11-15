#!/usr/bin/env pybricks-micropython
from spockbots.motor import SpockbotsMotor
import time
from spockbots.output import led, PRINT

from spockbots.gyro import SpockbotsGyro as Gyro

from spockbots.output import PRINT

"""GYRO-ANG GYRO-RATE GYRO-FAS GYRO-G&A GYRO-CAL TILT-RATE TILT-ANG"""


def run_swing():
    """
    Activate the seing, place the white block, go to the elevator, turn over the elevator
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

    def arm_motor(speed, degrees):
        robot.left_medium.run_angle(speed * 10, degrees)

    def six():
        return robot.color(2) in [6]

    def blue():
        return robot.color(2) in [2]

    def white():
        return robot.value(2) >= 90

    gyro.forward(25, 30)
    gyro.turn(10, -15)
    gyro.forward(25, 16)
    robot.turntowhite(15, direction="right", port=3)
    robot.turntoblack(15, direction="right", port=3)
    robot.turntowhite(15, direction="left", port=3)

    robot.followline_pid(distance=30, speed=10, kp=0.30, ki=0.0, kd=0.0)

    gyro.forward(speed=25, distance=1.8, finish=blue, min_speed=1, acceleration=2)
    gyro.forward(speed=25, distance=10.6, finish=white, min_speed=1, acceleration=2)
    gyro.forward(speed=25, distance=11, finish=blue, min_speed=1, acceleration=2)
    robot.beep()
    robot.beep()

    robot.turntoblack(15, direction="right", port=3)

    robot.followline_pid(distance=20, speed=10, kp=0.30, ki=0.0, kd=0.0)

    robot.beep()
    gyro.forward(speed=25, distance=9.5)
    gyro.turn(30, 45)
    robot.forward(25, -25)
    gyro.turn(25, 33)

    robot.forward(25, -10)
    gyro.turn(100, 60)
    gyro.turn(25, 45)
    gyro.forward(speed=100, distance=135)


if __name__ == "__main__":
    time_start = time.time()
    run_swing()
    time_end = time.time()
    print("Time:", time_end - time_start)

    # Time: 43.13