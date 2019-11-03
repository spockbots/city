from spockbots.motor import SpockbotsMotor
import time

robot = SpockbotsMotor()
robot.setup()

print(robot)

""""
robot.forward(25, 20)
robot.forward(25, -20)
robot.forward(25, 20)
robot.forward(25, -20)
robot.turn(25, 90)
robot.turn(25, -90)

robot.gotoblack(25, 3)
"""

# robot.color.flash()


robot.followline(speed=20, port=3, distance=40)


time.sleep(1)
