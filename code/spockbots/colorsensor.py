#!/usr/bin/env micropython

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, 
from ev3dev2.motor import MoveTank, SpeedPercent
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4
from ev3dev2.button import Button
from time import sleep


class SpockbotsColorSensor:

    def __init__(self, port, speed=5):
        """

        :param port:
        :param speed:
        """
        """
        :param: number  number of color sensor on ev3
        """
        if port == 2:
            self.sensor = ColorSensor(INPUT_2)
        elif port == 3:
            self.sensor = ColorSensor(INPUT_3)
        elif port == 4:
            self.sensor = ColorSensor(INPUT_4)
        
        self.port = port
        self.black = 1000
        self.white = 0
        self.speed = speed
        self.sensor.mode='COL-REFLECT'

    def set_white(self):
        value = self.sensor.reflected_light_intensity
        if value > self.white:
            self.white = value 
    
    def set_black(self):
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
        return c
    
    def calibrate(self):

        button=Button()

        colorsensor = SpockbotsColorSensor(self.port)

        tank = MoveTank(OUTPUT_A, OUTPUT_B)
        tank.left_motor.polarity='inversed'
        tank.right_motor.polarity='inversed'

        while True:

            txt = "exit"
            if button.check_buttons(buttons=['backspace']):
                break
            else:
                txt = "Press Backspace to Stop"

            #print("%s 2: %3d"  % ( txt, colorsensor[2].value(), "\n"))


            colorsensor.set_white()
            colorsensor.set_black()

        tank.off()

        f= open("colcal2.txt","w+")
        f.write("%3d, %3d" % (colorsensor.black, colorsensor.white))
        f.close()
        return colorsensor

    def clear(self):
        f= open("/home/robot/calibrate.txt","w")
        f.close()

    
class SpockbotsColorSensors:


    def __init__(self, ports=[2,3,4], speed=5):
        self.ports=ports
        self.speed = speed
        self.colorsensor = [0,0,0,0,0]

        for i in ports:
            self.colorsensor[i] = SpockbotsColorSensor(i)


    def value(i):
        return self.colorsensor[i].value()

    def calibrate(self, ports=[2,3,4]):

        button=Button()

        tank = MoveTank(OUTPUT_A, OUTPUT_B)
        tank.left_motor.polarity='inversed'
        tank.right_motor.polarity='inversed'
        tank.on(SpeedPercent(self.speed), SpeedPercent(self.speed))

        while True:

            txt = "exit"
            if button.check_buttons(buttons=['up', 'down']):
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


    def write(self):

        f= open("/home/robot/calibrate.txt","w")
        for i in ports:
            f.write(str(self.colorsensor[i].black)+"\n")
            f.write(str(self.colorsensor[i].white)+"\n")
        f.close()


    def clear(self):
        f= open("/home/robot/calibrate.txt","w")
        f.close()


    def read(self):
        f= open("/home/robot/calibrate.txt","r")
        for i in self.ports:
            self.colorsensor[i].black = int(f.readline())
            self.colorsensor[i].white = int(f.readline())
        f.close()



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




