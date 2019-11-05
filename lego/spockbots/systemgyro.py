import os
import spockbots.robot as robot

from spockbots.output import led
from spockbots.output import beep


class Gyro(object):

    def __init__(self):
        self.sensor = None

    def connect(self):

        print("Find Gyro", self.sensor)
        connected = False
        while not connected:
           if self.sensor is None:
                self.sensor = self.info()
           else:
               break
        print("Find Gyro found", self.sensor)

        self.sensor = self.info()

    def reset(self):


        # "GYRO-CAL",
        for kind in ["GYRO-ANG", "GYRO-G&A"]:
            self.mode(kind)
            try:
                a, s = self.get()
            except:
                print("READ ERROR")

    def get(self):
        self.angle = robot.readfile("/sys/class/lego-sensor/" + self.sensor +  "/value0")
        self.rate = robot.readfile("/sys/class/lego-sensor/" + self.sensor +  "/value1")
        return self.angle, self.rate

    def angle(self):
        self.angle = robot.readfile("/sys/class/lego-sensor/sensor12/value0")
        return self.angle

    def rate(self):
        self.rate = robot.readfile("/sys/class/lego-sensor/sensor12/value1")
        return self.rate

    def info(self):

        # find gyro

        sensors = os.listdir("/sys/class/lego-sensor/")
        id = None
        for sensor in sensors:
            data = robot.readfile("/sys/class/lego-sensor/" + sensor + "/mode")
            print(sensor, ";", data)
            if "GYRO" in data or "TILT" in data:
                id = sensor
        print()
        print("GYRO", sensor)
        for directive in ['address',
                          'bin_data',
                          'bin_data_format',
                          'command',
                          'commands',
                          'decimals',
                          'device',
                          'direct',
                          'driver_name',
                          'fw_version',
                          'mode',
                          'modes',
                          'num_values',
                          'poll_ms',
                          'power',
                          'subsystem',
                          'text_value',
                          'uevent',
                          'units',
                          'value0',
                          'value1',
                          'value2',
                          'value3',
                          'value4',
                          'value5',
                          'value6',
                          'value7']:
            try:
                data = robot.readfile("/sys/class/lego-sensor/" + id + "/" + directive)
                print(directive, ":", data)
            except:
                pass
            return id

    def mode(self, kind):
        """
        GYRO-G&A GYRO-ANG GYRO-RATE GYRO-CAL

        Not supported: GYRO-FAS  TILT-RATE TILT-ANG

        :param kind:
        :return:
        """
        kind = kind.replace("&", "\\&")
        robot.writefile("/sys/class/lego-sensor/" + self.sensor + "/mode", kind)
