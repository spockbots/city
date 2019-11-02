#!/usr/bin/env python3

import spockbots.robot as robot
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4
import time

from spockbots.colorsensor import SpockbotsColorSensor,  SpockbotsColorSensors
from spockbots.robot import button_wait, direction, beep
import spockbots.robot as robot

from ev3dev2.sound import Sound

robot.beep()
robot.read()

robot.colorsensors.info()


#robot.followline(run=True, steering=15, black=15, speed=10, port=3)
robot.followline_simple(run=True, steering=15, black=15, speed=10, port=3)

#sensor = SpockbotsColorSensor(4)
#sensor.flash()

time.sleep(1)
robot.beep()



