from spockbots.motor import SpockbotsMotor
import time

robot = SpockbotsMotor()
robot.setup()

print(robot)

robot.forward(25, 20)
robot.forward(25, -20)
robot.forward(25, 20)
robot.forward(-25, 20)
robot.turn(25, 90)
robot.turn(25, -90)

time.sleep(1)
