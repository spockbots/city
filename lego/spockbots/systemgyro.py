import os
import spockbots.robot as robot
from spockbots.output import PRINT

from spockbots.output import led
from spockbots.output import beep

from spockbots.output import readfile, writefile


class Gyro(object):

    def __init__(self):
        """

        """
        self.sensor = None
        self.last_angle = 0
        self.last_rate = 0

    def connect(self):
        """

        :return:
        """

        PRINT("GYRO CONNECT", self.sensor)
        connected = False
        while not connected:
            if self.sensor is None:
                self.sensor = self.info()
            else:
                break
        PRINT("GYRO CONNECT. ok", self.sensor)

    def reset(self):
        """

        :return:
        """
        PRINT("GYRO RESET")
        a = -360
        s = -100
        while a != 0 and s != 0:
            try:
                self.mode("GYRO-ANG")
                self.mode("GYRO-G&A")
                a, s = self.get()
            except:
                PRINT("Gyro read error, zero")

        PRINT("GYRO RESET. ok", a, s)
        return a, s

    def get(self):
        """

        :return:
        """
        angle = self.angle()
        rate = self.rate()
        return angle, rate

    def angle(self):
        """

        :return:
        """
        try:
            angle = int(readfile("/sys/class/lego-sensor/" + self.sensor + "/value0"))
            self.last_angle = angle
        except:
            print("ANGLE ERROR")
            angle = self.last_angle
        return angle

    def rate(self):
        """

        :return:
        """
        try:
            rate = int(readfile("/sys/class/lego-sensor/" + self.sensor + "/value1"))
            self.last_rate = rate
        except:
            print("RATE ERROR")
            rate = self.last_rate
        return rate

    def still(self, count=10, still=5):
        """

        :param count:
        :param still:
        :return:
        """
        still_count = 0
        i = count
        while i > 0:
            value = self.rate()
            if value == 0:
                still_count = still_count + 1
            i = i - 1
        PRINT("STILL:", still_count, "of", count)
        return still_count >= still

    def info(self):
        """

        :return:
        """

        # find gyro

        sensors = os.listdir("/sys/class/lego-sensor/")
        sensor_id = None
        for sensor in sensors:
            location = "/sys/class/lego-sensor/" + sensor + "/mode"
            data = readfile(location)
            PRINT(sensor + ":" + data, location)
            if "GYRO" in data or "TILT" in data:
                sensor_id = sensor
                PRINT("")
                PRINT("GYRO:", sensor, data)
                break
        for directive in ['address',
                          # 'bin_data',
                          'bin_data_format',
                          # 'command',
                          # 'commands',
                          'decimals',
                          # 'device',
                          # 'direct',
                          'driver_name',
                          # 'fw_version',
                          'mode',
                          'modes',
                          'num_values',
                          # 'poll_ms',
                          # 'power',
                          # 'subsystem',
                          # 'text_value',
                          'uevent',
                          # 'units',
                          'value0',
                          'value1',
                          # 'value2',
                          # 'value3',
                          # 'value4',
                          # 'value5',
                          # 'value6',
                          # 'value7'
                          ]:
            try:
                data = readfile("/sys/class/lego-sensor/" + sensor_id + "/" + directive)
                PRINT(directive, ":", data)
            except:
                PRINT(directive, ":", "not found")
        return sensor_id

    def mode(self, kind):
        """
        GYRO-G&A GYRO-ANG GYRO-RATE GYRO-CAL

        Not supported: GYRO-FAS  TILT-RATE TILT-ANG

        :param kind:
        :return:
        """
        # kind = kind.replace("&", "\\&")
        writefile("/sys/class/lego-sensor/" + self.sensor + "/mode", kind)

    def test(self, n):
        """

        :param n:
        :return:
        """
        counter = 0
        while counter < n:
            angle, rate = self.get()

            PRINT("GYRO TEST:", counter, angle, rate)
            counter = counter + 1
