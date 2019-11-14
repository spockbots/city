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
    robot.colorsensors.read()

    print(robot)

    #
    # setup gyro
    #
    gyro = Gyro(robot)
    gyro.setup()

    gyro.forward(30, 85)
    robot.gotowhite(25, 2, 90)
    gyro.forward(25, 5)
    gyro.turn(10, 10)

    robot.turntowhite(10, "left", 2, 90)
    robot.turntoblack(10, "left", 2, 5)
    robot.turntowhite(10, "right", 2, 90)

    robot.followline(speed=10, distance=15, port=2, right=True)
    gyro.turn(10, -85)
    gyro.forward(10, 6)
    
    robot.forward(10, -10)
    gyro.turn(10, 100)
    robot.forward(75, -140)

    # move a long distance
    #robot.forward(30,85)
    # trun towards the white line
    #robot.turn(25,-45)
    # move a bit forward so we are not in the red circle as it colld be interpreted as white
    #robot.forward(25,23)

    # back up and leave the building
    #robot.forward(25,-15)
    # turn to home
    #robot.turn(25, 15)
    # go back to base
    #robot.forward(100, -100)






if __name__ == "__main__":
    run_tan_circle()
