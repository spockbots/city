#!/usr/bin/env python3

# from http://thetechnicgear.com/2014/03/howto-create-line-following-robot-using-mindstorms/

from ev3dev2.motor import LargeMotor, SpeedPercent
from ev3dev2.motor import OUTPUT_A, OUTPUT_B

import spockbots.robot as robot



motor_left = LargeMotor(OUTPUT_B)
motor_right = LargeMotor(OUTPUT_A)


robot.beep()
robot.read()
robot.colorsensors.info()
#robot.colorsensors.flash(ports=[3])

#robot.followline_1(t=3, port=3, speed=25, factor=2.0, black=0, white=100)
#robot.followline_1(t=2, port=3, speed=25, factor=3.0, black=0, white=100)
robot.followline_1(t=2, port=3, speed=25, factor=1.9, black=0, white=100)


robot.followline_2(t=3, port=3, speed=25, black=0, white=100, kp=0.35)

robot.followline_3(t=3.0, port=3, speed=25,black=0, white=100, kp=0.35, ki=0.02, kd=0.0)

robot.followline_4(t=10.0, port=3,
				   speed=25,
				   black=0, white=100,
                   kp=3.0, ki=0.01, kd=0.0)

robot.followline_5(t=3, port=3, speed=25, black=0, white=100, delta=-35, factor=0.7)
robot.followline_5(t=3, port=3, speed=25, black=0, white=100, delta=-35, factor=0.4)