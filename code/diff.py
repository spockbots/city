#!/usr/bin/env python3

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, MoveDifferential, SpeedPercent
from spockbots.wheel import SpockbotsTire

STUD_MM = 8

# test with a robot that:
# - uses the standard wheels known as EV3Tire
# - wheels are 16 studs apart


mdiff = MoveDifferential(OUTPUT_A, OUTPUT_B, SpockbotsTire, 14 * STUD_MM)
mdiff.odometry_start()


def direction(movement):
    """
    Sets the direction of the robot

    :param movement: either 'front' or 'back'
    :return:
    """
    if movement == 'front':
        mdiff.left_motor.polarity = 'inversed'
        mdiff.right_motor.polarity = 'inversed'
    elif movement == 'back':
        mdiff.left_motor.polarity = 'normal'
        mdiff.right_motor.polarity = 'normal'


def forward(speed=50, distance=10, brake=True):
    mdiff.on_for_distance(SpeedPercent(speed), 10 * distance, brake=brake)

def move(speed, x,y, brake=True):
    mdiff.on_to_coordinates(SpeedPercent(speed), 10 * y, 10 * x, brake=brake)

def relative_move(speed, x,y, brake=True):
    mdiff.odometry_start()
    move(speed, x, y, brake=brake)
    mdiff.odometry_stop()



# Rotate 90 degrees clockwise
#mdiff.turn_right(SpeedRPM(40), 90)

# Drive forward 500 mm
#direction('front')
#forward(25, distance=5)
#direction('back')
#forward(25, distance=5)

# Drive in arc to the right along an imaginary circle of radius 150 mm.
# Drive for 700 mm around this imaginary circle.
#mdiff.on_arc_right(SpeedPercent(25), 150, 700)

# Enable odometry



# Use odometry to go back to where we started
#mdiff.on_to_coordinates(SpeedRPM(40), 0, 0)

# Use odometry to rotate in place to 90 degrees
#mdiff.turn_to_angle(SpeedRPM(40), 90)


direction('front')
move(40, 60, 20)
move(40, 0, 0)

# Disable odometry
mdiff.odometry_stop()