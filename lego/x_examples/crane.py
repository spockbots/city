#!/usr/bin/env pybricks-micropython
# from spockbots.motor import SpockbotsMotor
from time import sleep

robot = SpockbotsMotor()
robot.setup()
robot.color.read()

print(robot)

"""
robot.forward(50, 10)
robot.turn(25, 45)
robot.forward(50, 30)

print("LLLL")
robot.turn(25, -45)

robot.gotowhite(25, 3)
robot.gotoblack(10, 3)
robot.gotowhite(10, 3)

#robot.forward(5, 2)
#robot.forward(-20, 20)
#robot.right(20, 45)
#robot.forward(-75, 60)
"""

dt = 0.3

robot.turn(25, 50)
sleep(dt)

robot.forward(50, 20)
sleep(dt)

robot.turn(25, -10)
sleep(dt)

robot.forward(50, 15)
sleep(dt)

sleep(0.5)
