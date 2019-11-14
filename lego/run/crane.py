#!/usr/bin/env pybricks-micropython

from spockbots.motor import SpockbotsMotor
from time import sleep


def run_crane():
    """
    TBD
    """
    robot = SpockbotsMotor()
    robot.debug = True

    robot.setup()
    robot.colorsensors.read()

    print(robot)

    """
    robot.forward(50, 10)
    robot.turn(25, 45)
    robot.forward(50, 30)
    
    robot.turn(25, -45)
    
    robot.gotowhite(25, 3)
    robot.gotoblack(10, 3)
    robot.gotowhite(10, 3)
    
    #robot.forward(5, 2)
    #robot.forward(-20, 20)
    #robot.right(20, 45)
    #robot.forward(-75, 60)
    """

    dt = 0.0

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

    # sleep(0.2)

    # back to base

    robot.forward(5, -5)  # backup slowly
    robot.forward(75, -20)
    robot.turn(25, 45)
    robot.forward(75, -30)
    robot.turn(25, 45)
    robot.forward(75, -20)


if __name__ == "__main__":
    run_crane()
