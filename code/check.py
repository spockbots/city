#! /usr/bin/env micropython

import spockbots.robot as robot
from time import sleep

def check_robot():
    robot.beep()

    robot.speak('Large Motors')

    robot.speak('Left')
    robot.motor_left.on_for_seconds(25,1)

    robot.speak('Right')
    robot.motor_right.on_for_seconds(25,1)

    robot.speak('Medium Motors')

    robot.speak('Left')
    robot.mediummotor_left.on_for_seconds(25,1)

    robot.speak('Right')
    robot.mediummotor_right.on_for_seconds(25,1)

    robot.speak('Light')

    robot.speak('Left')
    robot.colorsensors.flash(ports=[2])

    robot.speak('Right')
    robot.colorsensors.flash(ports=[3])

    robot.speak('Back')
    robot.colorsensors.flash(ports=[4])

    robot.speak('finished')

