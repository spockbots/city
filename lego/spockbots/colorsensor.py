#!/usr/bin/env micropython

from time import sleep

from pybricks.parameters import Port

from pybricks.ev3devices import Motor, ColorSensor

#from ev3dev2.button import Button
#from ev3dev2.motor import MoveTank, SpeedPercent
#from ev3dev2.motor import OUTPUT_A, OUTPUT_B
##from ev3dev2.sensor import INPUT_2, INPUT_3, INPUT_4
#from ev3dev2.sensor.lego import ColorSensor
#from ev3dev2.sound import Sound


class SpockbotsColorSensor:

    def __init__(self, port, speed=5):
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
        self.speed = speed
        self.sensor.mode='COL-REFLECT'

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
        value = self.sensor.reflected_light_intensity
        if value < self.black:
            self.black = value 

    """def raw_value(self):
        if self.sensor.reflected_light_intensity >= 50:
            print("%3d" % (self.sensor.reflected_light_intensity, "\n"))
        sleep (5)
        return self.sensor.reflected_light_intensity
    """

    def value(self):
        """
        reads the current value mapped between 0 and 100
        :return:
        """
        val = self.sensor.reflected_light_intensity
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
    
    def calibrate(self, direction='front'):
        """
        runs over the lines and finds the largest black and white value
        :param direction:
        :return:
        """

        button=Button()

        tank = MoveTank(OUTPUT_A, OUTPUT_B)

        if direction == 'front':
            tank.left_motor.polarity='inversed'
            tank.right_motor.polarity='inversed'
        else:
            tank.left_motor.polarity = 'normal'
            tank.right_motor.polarity = 'normal'

        while True:

            txt = "exit"
            if button.check_buttons(buttons=['backspace']):
                break
            else:
                txt = "Press Backspace to Stop"

            #print("%s 2: %3d"  % ( txt, colorsensor[2].value(), "\n"))


            self.sensor.set_white()
            self.sensor.set_black()

        tank.off()

        f= open("colcal2.txt","w+")
        f.write("%3d, %3d" % (self.black, self.white))
        f.close()

    def clear(self):
        f= open("/home/robot/calibrate.txt","w")
        f.close()

    def flash(self):
        """
        flashes the color sensor by switching between color and reflective mode
        """
        sound = Sound()
        sound.beep()

        self.sensor.mode = 'COL-COLOR'
        color = self.sensor.color
        sleep(0.5)

        self.sensor.mode = 'COL-REFLECT'
        light = self.sensor.reflected_light_intensity
        sleep(0.5)

    def write(self):
        """
        append the black and white value to a file
        """
        f= open("/home/robot/calibrate.txt","w+")
        f.write(str(self.sensor.black)+"\n")
        f.write(str(self.sensor.white)+"\n")
        f.close()

    def info(self):
        """
        prints the black and white value read form the sensor
        """
        print ("Cloorsensor", self.port, self.black, self.white)

    def read(self):
        """
        reads the color sensor data form the file
        :return:
        """
        try:
            f= open("/home/robot/calibrate.txt","r")
            self.colorsensor[port].black = int(f.readline())
            self.colorsensor[port].white = int(f.readline())
            f.close()
        except:
            print ("we can not find the calibration file")


class SpockbotsColorSensors:

    def __init__(self, ports=[2,3,4], speed=5):
        self.ports=ports
        self.speed = speed
        self.colorsensor = [0,0,0,0,0]
        self.ports = ports
        for i in ports:
            self.colorsensor[i] = SpockbotsColorSensor(i)

    def sensor(self, port):
        return self.colorsensor[port]

    def value(self, i):
        return self.colorsensor[i].value()

    def calibrate(self, ports=[2,3,4], direction='front'):


        print(direction)
        print(ports)
        print (self.speed)

        button=Button()

        tank = MoveTank(OUTPUT_A, OUTPUT_B)

        if direction == 'front':
            tank.left_motor.polarity='inversed'
            tank.right_motor.polarity='inversed'
        else:
            tank.left_motor.polarity = 'normal'
            tank.right_motor.polarity = 'normal'

        tank.on(SpeedPercent(self.speed), SpeedPercent(self.speed))



        while True:

            txt = "exit"
            if button.check_buttons(buttons=['backspace']):
                break
            else:
                txt = "Press Backspace to Stop"

            #print("%s 2: %3d"  % ( txt, colorsensor[2].value(), "\n"))

            for i in ports:
                self.colorsensor[i].set_white()
                self.colorsensor[i].set_black()
                print(i, self.colorsensor[i].black, self.colorsensor[i].white, sep=' ')

        tank.off()

        for i in ports:
            print(i, self.colorsensor[i].black, self.colorsensor[i].white)


    def write(self, ports=[2,3,4]):

        f= open("/home/robot/calibrate.txt","w")
        for i in ports:
            f.write(str(self.colorsensor[i].black)+"\n")
            f.write(str(self.colorsensor[i].white)+"\n")
        f.close()


    def clear(self):
        f= open("/home/robot/calibrate.txt","w")
        f.close()


    def read(self):
        try:
            f= open("/home/robot/calibrate.txt","r")
            for i in self.ports:
                self.colorsensor[i].black = int(f.readline())
                self.colorsensor[i].white = int(f.readline())
            f.close()
        except:
            print ("we can not find the calibration file")

    def flash(self, ports=[2,3,4]):
        for port in ports:
            self.colorsensor[port].flash()

    def info(self, ports=[2,3,4]):
        print("")
        print("Color sensor black and white values")
        print("")

        for port in ports:
            self.colorsensor[port].info()
        print()

    def test(self, ports=[2,3,4]):
        print("")
        print("Color sensor tests")
        print("")

        for port in ports:
            v = self.colorsensor[port].value()
            print ("Color sensor", port, v)
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




