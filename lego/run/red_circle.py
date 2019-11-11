#!/usr/bin/env pybricks-micropython

from spockbots.motor import SpockbotsMotor
from spockbots.gyro import SpockbotsGyro as Gyro
from time import sleep
from spockbots.output import led, PRINT

def run_red_circle():
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

    #followline(10, port=3, stop_color_sensor=2, stop_values=[7], stop_color_mode="color")


    # go forward overthe curve in line
    robot.forward(25, 35)

    # find the white lien so we can start with line following
    robot.turntowhite(25, direction="right", port=3)

    robot.followline(10, distance=30, port=3, right=False)
    robot.gotocolor(10, 2, colors=[7])
    robot.turn(10,-62)
    robot.forward(25,-10)
    robot.turn(50,45)
    robot.forward(100,-80)


if __name__ == "__main__":
    run_red_circle()
