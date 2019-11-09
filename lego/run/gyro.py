#!/usr/bin/env pybricks-micropython

from spockbots.gyro import SpockbotsGyro
#from spockbots.systemgyro import Gyro


import time
from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from time import sleep

from spockbots.output import PRINT

"""GYRO-ANG GYRO-RATE GYRO-FAS GYRO-G&A GYRO-CAL TILT-RATE TILT-ANG"""

def run_gyro():
    gyro = Gyro(1)
    gyro.reset()
    if gyro.still():
        PRINT("ROBOT STILL")
    else:
        PRINT("ROBOT DRIFT")

    #gyro.test(30)
    #gyro.reset()
    #gyro.test(10)

    # gyro.mode("GYRO-CAL")
    # gyro.test(5)

    # gyro.mode("GYRO-ANG")
    # gyro.test(5)

    # gyro.mode("GYRO-G&A")
    # gyro.test(5)
