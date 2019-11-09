#!/usr/bin/env pybricks-micropython

from spockbots.output import PRINT
from spockbots.gyro import SpockbotsGyro as Gyro
# from spockbots.systemgyro import Gyro

"""GYRO-ANG GYRO-RATE GYRO-FAS GYRO-G&A GYRO-CAL TILT-RATE TILT-ANG"""

gyro = Gyro()
# gyro.connect()
gyro.reset()
if gyro.still():
    PRINT("ROBOT STILL")
else:
    PRINT("ROBOT DRIFT")

gyro.test(30)

gyro.reset()
gyro.test(10)

# gyro.mode("GYRO-CAL")
# gyro.test(5)

# gyro.mode("GYRO-ANG")
# gyro.test(5)

# gyro.mode("GYRO-G&A")
# gyro.test(5)
