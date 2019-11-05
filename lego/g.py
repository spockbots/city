from spockbots.gyro import SpockbotsGyro
import time
from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from time import sleep

from spockbots.systemgyro import Gyro

from spockbots. import Gyro




"""GYRO-ANG GYRO-RATE GYRO-FAS GYRO-G&A GYRO-CAL TILT-RATE TILT-ANG"""


"""
gyro = Gyro()
gyro.reset()

def test(n):
    counter = 0
    while counter < n:
        angle, rate = gyro.get()

        print(counter, angle, rate)
        counter = counter + 1


gyro.mode("GYRO-CAL")
test(5)

gyro.mode("GYRO-ANG")
test(5)

gyro.mode("GYRO-G&A")
test(5)


counter = 0
test(1000)

#gyro.mode("GYRO-ANG")
#test(10)

#gyro.mode("GYRO-FAS")
#test(10)

#gyro.mode("TILT-ANG")
#test(10)

#gyro.mode("TILT-RATE")
#test(10)
"""


"""

gyro = SpockbotsGyro(1)
gyro.sysinfo()

#time.sleep(1)
#gyro.reset()

while True:
    time.sleep(0.2)
    print(gyro.angle(), gyro.drift())
    if gyro.drift():
        print("RESET")
        try:
            ultrasonic = UltrasonicSensor(Port.S1)
            ultrasonic.presence()
        except Exception as e:
            print (e)

        sleep(0.3)
        gyro = SpockbotsGyro(1)
"""