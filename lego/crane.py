from spockbots.motor import SpockbotsMotor
import time

robot = SpockbotsMotor()
robot.setup()

print(robot)

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



time.sleep(1)
