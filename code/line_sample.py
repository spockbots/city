# from http://thetechnicgear.com/2014/03/howto-create-line-following-robot-using-mindstorms/

from ev3dev2.motor import LargeMotor, SpeedPercent
from ev3dev2.motor import OUTPUT_A, OUTPUT_B

import spockbots.robot as robot


def followline_1(port=2, speed=50, factor=2, black=0, white=100)


	midpoint = ( white - black ) / 2 + black

	while True:

		value = robot.light(port)

		if value < midpoint:
			robot.motor_left.on(SpeedPercent(speed)
			robot.motor_right.on(SpeedPercent(int(speed/factor))
		else
            robot.motor_left.on(SpeedPercent(int(speed / factor))
            robot.motor_right.on(SpeedPercent(speed)


def followline_2(port=2, speed=50, black=0, white=100)

	midpoint = ( white - black ) / 2 + black
	kp=1.0

	while True:
	
		value = robot.light(port)
		correction = kp * ( midpoint - value ) 
		
		robot.steering.on(correction, speed)


def followline_3(port=2, speed=50, black=0, white=100,
                 kp=1.0, ki=1.0, kd=1.0):

    midpoint = ( white - black ) / 2 + black
    lasterror=0.0

	while True:

		value = robot.light(port)

		error = midpoint - value
		integral = error + integral
		derivative = error - lasterror
		
		correction = kp * error + ki * integral + kd * derivative
		
		robot.steering.on(correction, speed)
		
		lasterror = error
