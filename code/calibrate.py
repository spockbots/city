#!/usr/bin/env micropython

import spockbots.robot as robot
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4
import time

from spockbots.colorsensor import SpockbotsColorSensor,  SpockbotsColorSensors
from spockbots.robot import button_wait, direction, beep
import spockbots.robot as robot

from ev3dev2.sound import Sound

#robot.beep()



#robot.followline()C

#sensor = SpockbotsColorSensor(4)
#sensor.flash()



sensors = SpockbotsColorSensors(ports=[2,3,4])

#sensors.flash(ports=[2,3,4])

print("front")
robot.beep()
robot.button_wait("enter")

sensors.calibrate(ports=[2,3], direction='front')

print("back")
robot.beep()
robot.button_wait("enter")
sensors.calibrate(ports=[4], direction='back')


sensors.info(ports=[2,3,4])

sensors.clear()


sensors.write(ports=[2,3,4])

robot.beep()
robot.beep()

robot.button_wait("enter")
print()
print("test")

while (True):
    sensors.test(ports=[2,3,4])
    time.sleep(1)
    if robot.button('backspace'):
        break


#    color = sensor.color
#    print (color)



#    time.sleep(1)

#
