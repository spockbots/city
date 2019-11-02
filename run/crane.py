
import spockbots.robot as robot
import sys
import os
from importlib import reload

robot.setup()
robot.forward(50,10)
robot.right(25,45)
robot.forward(50,30)

robot.left(25,45)
robot.gotowhite(25,3)
robot.gotoblack(10,3)
robot.gotowhite(10,3)
robot.forward(5,2)
robot.forward(-20,20)
robot.right(20,45)
robot.forward(-75,60)