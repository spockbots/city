# from http://thetechnicgear.com/2014/03/howto-create-line-following-robot-using-mindstorms/

from ev3dev2.motor import LargeMotor, SpeedPercent
from ev3dev2.motor import OUTPUT_A, OUTPUT_B

import spockbots.robot as robot



motor_left = LargeMotor(OUTPUT_B)
motor_right = LargeMotor(OUTPUT_A)


robot.beep()
robot.read()
robot.colorsensors.info()


robot.followline_1(port=2, speed=25, factor=2, black=0, white=100)
#robot.followline_2(port=2, speed=50, black=0, white=100)
#robot.followline_3(port=2, speed=50, black=0, white=100,
#                 kp=1.0, ki=1.0, kd=1.0)
