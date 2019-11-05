#!/usr/bin/env micropython

from time import sleep

from pybricks import ev3brick as brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port


class SpockbotsColorSensor:

    def __init__(self, port=3):
        """

        :param port: the port
        :param speed: teh speed for calibartion
        """
        """
        :param: number  number of color sensor on ev3
        """
        if port == 1:
            self.sensor = ColorSensor(Port.S1)
        elif port == 2:
            self.sensor = ColorSensor(Port.S2)
        elif port == 3:
            self.sensor = ColorSensor(Port.S3)
        elif port == 4:
            self.sensor = ColorSensor(Port.S4)

        self.port = port
        self.black = 100
        self.white = 0

    def set_white(self):
        """
        sets the current value to white
        :return:
        """
        value = self.sensor.reflection()
        if value > self.white:
            self.white = value

    def set_black(self):
        """
        sets the current value to black
        """
        value = self.sensor.reflection()
        if value < self.black:
            self.black = value

    def reflection(self):
        return self.sensor.reflection()

    def light(self):
        return self.value()

    def value(self):
        """
        reads the current value mapped between 0 and 100
        :return:
        """
        val = self.sensor.reflection()
        b = self.black
        t1 = val - b
        t2 = self.white - self.black
        ratio = t1 / t2
        c = ratio * 100
        if c < 0:
            c = 0
        if c > 100:
            c = 100
        return int(c)

    def clear(self):
        f = open("/home/robot/calibrate.txt", "w")
        f.close()

    def flash(self):
        """
        flashes the color sensor by switching between color and reflective mode
        """


        brick.sound.beep()
        light = self.sensor.rgb()
        sleep(0.5)
        light = self.sensor.reflection()
        sleep(0.5)


    def write(self):
        """
        append the black and white value to a file
        """
        f = open("/home/robot/calibrate.txt", "w+")
        f.write(str(self.sensor.black) + "\n")
        f.write(str(self.sensor.white) + "\n")
        f.close()

    def info(self):
        """
        prints the black and white value read form the sensor
        """
        print("Cloorsensor", self.port, self.black, self.white)

    def read(self):
        """
        reads the color sensor data form the file
        :return:
        """
        try:
            f = open("/home/robot/calibrate.txt", "r")
            self.colorsensor[port].black = int(f.readline())
            self.colorsensor[port].white = int(f.readline())
            f.close()
        except:
            print("we can not find the calibration file")


class SpockbotsColorSensors:

    def __init__(self, ports=[2, 3, 4], speed=5):
        self.ports = ports
        self.speed = speed
        self.colorsensor = [0, 0, 0, 0, 0]
        self.ports = ports
        for i in ports:
            self.colorsensor[i] = SpockbotsColorSensor(port=i)

    def sensor(self, port):
        return self.colorsensor[port]

    def value(self, i):
        return self.colorsensor[i].value()

    def write(self, ports=[2, 3, 4]):

        f = open("/home/robot/calibrate.txt", "w")
        for i in ports:
            f.write(str(self.colorsensor[i].black) + "\n")
            f.write(str(self.colorsensor[i].white) + "\n")
        f.close()

    def clear(self):
        f = open("/home/robot/calibrate.txt", "w")
        f.close()

    def read(self):
        try:
            f = open("/home/robot/calibrate.txt", "r")
            for i in self.ports:
                self.colorsensor[i].black = int(f.readline())
                self.colorsensor[i].white = int(f.readline())
            f.close()
        except:
            print("we can not find the calibration file")
            self.colorsensor[2].black = 9
            self.colorsensor[2].white = 100
            self.colorsensor[3].black = 10
            self.colorsensor[3].white = 100
            self.colorsensor[4].black = 4
            self.colorsensor[4].white = 48
            print("Using the following defaults")
            self.info()


    def flash(self, ports=[2, 3, 4]):
        for port in ports:
            self.colorsensor[port].flash()

    def info(self, ports=[2, 3, 4]):
        print("")
        print("Color sensor black and white values")
        print("")

        for port in ports:
            self.colorsensor[port].info()
        print()

    def test(self, ports=[2, 3, 4]):
        print("")
        print("Color sensor tests")
        print("")

        for port in ports:
            v = self.colorsensor[port].value()
            print("Color sensor", port, v)
        print()

# from spockbots.colorsensor import SpockbotsColorSensors
# 
#  calibration
# 
#  colersensors = SpockbotsColorSensors()
#  colorsensors.calibrate([2,3])
#
# rotate the robot
# position it before the line
#
#  colorsensors.calibrate([4])
#  colorsensors.write()
#
# use
#
#  colersensors = SpockbotsColorSensors()
#  colorsensors.read()
#
#  colorsensor.value(2)
