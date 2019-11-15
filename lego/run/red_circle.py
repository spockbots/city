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

    gyro.forward(25, 62)
    gyro.turn(10, -30)
    robot.forward(10, -10)
    gyro.turn(10, 45)
    robot.forward(75, -70)

    # def till_tan():
    #    v = robot.colorsensors.color(2) in [7]
    #    print("TAN", v)
    #    return v

    # gyro.forward(speed=25, distance=82, finish=till_tan)
    # robot.turntocolor(10, direction="left", port=3, colors=[1])

    # followline(10, port=3, stop_color_sensor=2, stop_values=[7], stop_color_mode="color")

    # go forward overthe curve in line
    # go forward over the black line and reliably set up for line following

    # robot.gotowhite(10, 3, white=90)
    # robot.gotoblack(10, 3, black=10)
    # robot.gotowhite(10, 3, white=90)
    # gyro.forward(10, 4)

    # robot.turntoblack(10, direction="right", port=3)
    # robot.turntowhite(25, direction="left", port=3)

    # find the white lien so we can start with line following
    # robot.turntowhite(25, direction="right", port=3)

    # robot.followline(10, distance=10, port=3, right=False)
    # robot.gotocolor(10, 2, colors=[7])
    # robot.turn(10,-62)
    # robot.forward(25,-10)
    # robot.turn(50,45)
    # robot.forward(100,-80)


if __name__ == "__main__":
    time_start = time.time()
    run_red_circle()
    time_end = time.time()
    print("Time:", time_end - time_start)
