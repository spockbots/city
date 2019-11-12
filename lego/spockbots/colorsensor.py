#!/usr/bin/env micropython

from time import sleep

from pybricks import ev3brick as brick
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Port


class SpockbotsColorSensor:
    """
    defines
    """

    def __init__(self, port=3):
        """

        :param port: the port
        :param speed: teh speed for calibration
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
        """

        :return:
        """
        return self.sensor.reflection()

    def light(self):
        """

        :return:
        """
        return self.value()

    def color(self):
        """

        :return:
        """
        return self.sensor.color()

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

    def flash(self):
        """
        flashes the color sensor by switching between
        color and reflective mode
        """

        brick.sound.beep()
        light = self.sensor.rgb()
        sleep(0.3)
        light = self.sensor.reflection()
        sleep(0.3)

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
        prints the black and white value read form the
        sensor
        """
        print("colorsensor",
              self.port,
              self.black,
              self.white)

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
    """

    This is how we create the sensors:

        colorsensor = SpockbotsColorSensors(ports=[2,3,4])
        colorsensor.read()

    Now you can use

        colorsensor[i].value()

    to get the reflective value of the colorsensor on port i.
    To get the color value we can use

        colorsensor[i].color()

    """

    def __init__(self, ports=[2, 3, 4], speed=5):
        """
        Creates the color sensors for our robot.
        Once calibrated, the sensor values always return 0-100,
        where 0 is black and 100 is white

        :param ports: the list of ports we use on the robot for color sensors
        :param speed: The speed for the calibration run
        """
        self.ports = ports
        self.speed = speed
        self.colorsensor = [0, 0, 0, 0, 0]
            # in python lists start from 0 not 1
            # so we simply do not use the firts element in the list
        # our robot uses only
        #  colorsensor[2]
        #  colorsensor[3]
        #  colorsensor[4]
        #  the ports are passed along as a list [2,3,4]
        self.ports = ports
        for i in ports:
            self.colorsensor[i] = SpockbotsColorSensor(port=i)

    def value(self, i):
        """
        returns the reflective value between 0-100 after
        calibration on the port i

        :param i: number of the port
        :return: the reflective color value
        """
        return self.colorsensor[i].value()

    def color(self, i):
        """
        returns the color value between 0-100 after
        calibration on the port i

        :param i: number of the port
        :return: The color value, blue = 2
        """
        return self.colorsensor[i].color()

    def write(self, ports=[2, 3, 4]):
        """
        writes the black and white values to the file
        calibrate.txt

        :param ports: the ports used to write
        """

        f = open("/home/robot/calibrate.txt", "w")
        for i in ports:
            f.write(str(self.colorsensor[i].black) + "\n")
            f.write(str(self.colorsensor[i].white) + "\n")
        f.close()

    def clear(self):
        """
        removes the file calibrate.txt
        """
        f = open("/home/robot/calibrate.txt", "w")
        f.close()

    def read(self, ports=[2, 3, 4]):
        """
        reads the black and white values to the file
        calibrate.txt

        The values must be written previously. If the file
        does not exists a default is used.
            2: 0, 100
            3: 0, 100
            4: 4, 40    # because it is higher up so white does
                          not read that well
        """
        try:
            f = open("/home/robot/calibrate.txt", "r")
            for i in ports:
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
        """
        Flashes the light sensor on teh ports one after another

        :param ports: the list of ports to flash
        """
        for port in ports:
            self.colorsensor[port].flash()

    def info(self, ports=[2, 3, 4]):
        """
        prints the information for each port, e.g.
        the minimal black and maximum while values
        :param ports: the list of ports to flash
        """
        print("")
        print("Color sensor black and white values")
        print("")

        for port in ports:
            self.colorsensor[port].info()
        print()

    def test_reflective(self, ports=[2, 3, 4]):
        """
        prints the reflective value of all senors between 0-100

        :param ports: the list of ports
        """
        print("")
        print("Color sensor tests")
        print("")

        for port in ports:
            v = self.colorsensor[port].value()
            print("Color sensor", port, v)
        print()

    def test_color(self, ports=[2, 3, 4]):
        """
        prints the color value of all senors between 0-100

        :param ports: the list of ports
        """
        print("")
        print("Color sensor tests")
        print("")

        for port in ports:
            v = self.colorsensor[port].value()
            print("Color sensor", port, v)
        print()

