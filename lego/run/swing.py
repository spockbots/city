#!/usr/bin/env pybricks-micropython
from spockbots.motor import SpockbotsMotor
import time
from spockbots.output import led, PRINT

from spockbots.gyro import SpockbotsGyro as Gyro

from spockbots.output import PRINT

"""GYRO-ANG GYRO-RATE GYRO-FAS GYRO-G&A GYRO-CAL TILT-RATE TILT-ANG"""


def run_swing():
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
    # gyro.connect()
    gyro.reset()
    if gyro.still():
        PRINT("ROBOT STILL")
    else:
        PRINT("ROBOT DRIFT")
        led("RED")
        robot.beep()
        robot.beep()
        robot.beep()

    dt = 1.0

    def wait():
        time.sleep(dt)
        robot.beep()

    # PUT IN COLOR CALIBRATE VALUES

    # go forward overthe curve in line
    robot.forward(25, 35)

    # find the white lien so we can start with line following
    robot.turntowhite(25, direction="right", port=3)

    # follow the line but stop before the dent
    robot.followline(speed=10, distance=45, port=3, right=False, delta=-35, factor=0.4)

    # move over the dent
    robot.forward(25,30)

    # find the line reliably
    robot.turn(10, -5)
    robot.turntoblack(25, direction="right", port=3)
    robot.turntowhite(25, direction="left", port=3)

    # follow the line and hit the swing
    robot.followline(speed=10, distance=16, port=3, right=False, delta=-35, factor=0.4)
    robot.forward(10, 5)

    # turn to knock out strut and place building
    robot.turn(25,30)

    # back up
    robot.forward(70, -25)

    # turn to elevator
    robot.turn(25, -30)
    # find the black line
    robot.turntoblack(25, direction="left", port=2)
    # follow the line to the elevator
    robot.followline(speed=10, distance=13,
                     port=2, right=True,
                     delta=-35, factor=0.4)

    # turn to the elevator
    robot.turn(25, 90)
    # move toward the elavator to position arm
    robot.forward(20, -15)

    # turn the elevator and turn home at the same time
    robot.turn(75, 130)
    # go home
    robot.forward(100, 130)



if __name__ == "__main__":
    run_swing()
