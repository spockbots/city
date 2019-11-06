from time import sleep

from pybricks.parameters import Port

from pybricks import ev3brick as brick
from pybricks.parameters import Direction
import sys
from pybricks.ev3devices import GyroSensor

import os
import glob


#######################################################
# Gyro
#######################################################

class SpockbotsGyro(object):
    # The following link gives some hine why it does not work fo rthe Gyror in mindstorm
    # http://ev3lessons.com/en/ProgrammingLessons/advanced/Gyro.pdf

    # in python we have three issues

    # sensor value is not 0 after reset
    # sensor value drifts after reset as it takes time to settle down
    # sensor value is not returned as no value is available from the sensor

    # This code fixes it.

    def __init__(self, port, direction="front"):
        """
        Initializes the Gyro Sensor
        :param gyro: The gyro sensor on a given port
        """

        if direction == "front":
            sensor_direction = Direction.CLOCKWISE
        else:
            sensor_direction = Direction.COUNTERCLOCKWISE

        found = False
        while not found:
            print("FINDING GYRO")
            try:
                if port == 1:
                    self.sensor = GyroSensor(Port.S1, sensor_direction)
                elif port == 2:
                    self.sensor = GyroSensor(Port.S2, sensor_direction)
                elif port == 3:
                    self.sensor = GyroSensor(Port.S3, sensor_direction)
                elif port == 4:
                    self.sensor = GyroSensor(Port.S4, sensor_direction)
                print("SENSOR:", self.sensor)
                sleep(0.1)
                self.sensor.reset_angle(0)
                found = True
            except Exception as e:
                print(e)
                if "No such sensor on Port" in str(e):
                    print()
                    print("ERROR: THe Gyro Sensor is disconnected")
                    print()
                    sys.exit()

        self.last_angle = -1000  # just set the current value to get us started
        print("GYRO INITIALIZED")

    def angle(self):
        """
        Gets the angle

        :return: The angle in degrees
        """
        try:
            s = self.sensor.speed()
            a = self.sensor.angle()
            print("AS", a, s)
            self.last_angle = a
        except:
            print("Gyro read error")
            a = self.last_angle

        return a

    def zero(self):
        """
        set the gyro angle to 0
        :return:
        """
        self.sensor.reset_angle(0)

        angle = 1000
        while angle != 0:
            sleep(0.1)
            angle = self.angle()

    def drift(self):
        """

        :return:
        """
        while True:  # loop in case we get a read error from the gyro speed
            try:
                speed = self.sensor.speed()
                if speed == 0:
                    return False  # no dift if the speed is 0
                else:
                    return True  # DRIFT IF THE SPEED IS NOT 0
            except:
                print("ERROR: DRIFT no value found")  # No speed value found, so repeat

    def status(self, count=10):
        """

        :param count:
        :return:
        """
        last = self.angle()
        i = 0
        still = 0
        drift = 0
        while i <= count:
            angle = self.angle()
            if angle == last:
                still = still + 1
                drift = 0
            else:
                drift = drift + 1
            i = i + 1
        print("GYRO STATUS", i, still, drift)
        return still >= count, drift >= count

    def reset(self):
        """
        safely resets the gyro
        :return:
        """

        self.sensor.reset_angle(0)
        try:
            self.last_angle = angle = self.sensor.angle()
        except:
            print("Gyro read error", angle)
            self.last_angle = angle = -1000

        count = 10
        while count >= 0:
            sleep(0.1)
            try:
                angle = self.sensor.angle()
            except:
                print("Gyro read error", angle)
            print(count, "Gyro Angle: ", angle)
            if angle == 0:
                count = count - 1
        self.last_angle = angle
        print("Gyro Angle, final: ", angle)

    def left(self, speed=25, degrees=90, offset=0):
        """
        The robot turns left with the given number of degrees

        :param speed: The speed
        :param degrees: The degrees
        """
        if speed == 25:
            offset = 8

        self.zero()

        tank.on(-speed, speed)
        angle = self.angle()
        print(angle, -degrees + offset)
        while angle > -degrees + offset:
            # print(angle, -degrees + offset)
            angle = self.angle()
        tank.off()
        tank.wait_while('running')

    def right(self, speed=25, degrees=90, offset=0):
        """
        The robot turns right with the given number of degrees

        :param speed: The speed
        :param degrees: The degrees
        """
        if speed == 25:
            offset = 8

        self.zero()

        tank.on(speed, -speed)
        angle = self.angle()
        print(angle, degrees - offset)
        while angle < degrees - offset:
            # print(angle, degrees - offset)
            angle = self.angle()
        tank.off()
        tank.wait_while('running')
