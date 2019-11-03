#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from pybricks.parameters import Stop, Direction

from pybricks.parameters import Button, Color
from time import sleep
import math
# ImageFile, SoundFile
import os
import time

#######################################################
# Motor
#######################################################

from spockbots.motor import left_motor
from spockbots.motor import right_motor
from spockbots.motor import tank
from spockbots.motor import distance_to_rotation
from spockbots.motor import distance_to_angle
from spockbots.motor import angle_to_distance
from spockbots.motor import on
from spockbots.motor import stop
from spockbots.motor import forward
from spockbots.motor import reset_motors
from spockbots.motor import diameter
from spockbots.motor import width
from spockbots.motor import circumference
from spockbots.motor import axle_track


#######################################################
# Sound
#######################################################

# sound = Sound()

"""
def speak(text):
    sound.speak(text)


def sing(song):
    sound.play_song(song)


def wav(source):
    sound.play_file("/home/robot/wav/" + source)
"""


def beep():
    """
    The robot will make a beep
    """
    brick.sound.beep()


def sound(pitch=1500, duration=300):
    brick.sound.beep(pitch, duration)


#######################################################
# LED
#######################################################

def led(group, color, brightness=255):
    """
    The robot will switch on the LEDS with the given color

    :param group: LED's can be on the LEFT or RIGHT
    :param color: the color to be used. One of
                  BLACK
                  RED
                  GREEN
                  AMBER
                  ORANGE
                  YELLOW
    """

    def switch(brightness, led, color):
        os.system("echo {} >  /sys/class/leds/led{}\:{}\:brick-status/brightness".format(brightness, led, color))



    # direction, LEFT
    # Color: GREEN, RED
    if color == "RED":
        c = Color.RED
    elif color == "GREEN":
        c = Color.GREEN
    elif color == "BLACK":
        c = Color.BLACK
    elif color == "YELLOW":
        c = Color.YELLOW
    elif color == "OFF":
        c = None

    """
    echo 0 >  /sys/class/leds/led0\:green\:brick-status/brightness 

    """
    brick.light(c)


def flash():
    """
    The robot will flash the LEDs and beep twice
    """
    beep()
    for color in ["BLACK", "RED", "GREEN"]:
        led("LEFT", color)
        led("RIGHT", color)
        sleep(0.1)
    beep()


#######################################################
# LCD
#######################################################

def clear():
    brick.display.clear()


def Print(text, x=None, y=None):
    if x is not None and y is not None:
        brick.display.text(text, (x, y))
    else:
        brick.display.text(text)

def font(size):

    s = "14"
    if size == 14:
        s = "14"
    elif size == 32:
        s = "32x16"
    os.system('setfont Lat15-TerminusBold' + s)


#######################################################
# Voltage
#######################################################

def voltage():
    voltage = brick.battery.voltage() / 1000
    Print("Voltage: " + str(voltage) + " V", 10, 20)


#######################################################
# Turn
#######################################################

def turn(speed, angle):
    """
    takes the radius of the robot and dives on it for a distance based on the ancle
    :param speed:
    :param angle:
    :return:
    """
    reset_motors()

    c = axle_track * math.pi
    fraction = 360.0 / angle
    d = c / fraction
    a = distance_to_angle(d) / 10.0

    left_motor.run_angle(speed * 10, -a, Stop.BRAKE, False)
    right_motor.run_angle(speed * 10, a, Stop.BRAKE, False)

    while abs(left_motor.angle()) < abs(a) and abs(left_motor.angle()) < abs(a):
        pass
    stop()


#######################################################
# Line
#######################################################

def followline(
        speed=25,  # speed 0 - 100
        t=None,  # time in seconds
        distance=None,  # distance in cm
        port=3,  # the port number we use to follow the line
        right=True,
        black=0,  # minimal balck
        white=100,  # maximal white
        delta=-35,  # paramaters to control smoothness
        factor=0.7):  # parameters to control smoothness

    print (distance)

    if right:
        f = - 1.0
    else:
        f = 1.0

    current = time.time()  # the current time
    if t is not None:
        end_time = current + t  # the end time

    reset_motors()

    while True:
        value = light(port)  # get the light value

        # correction = delta + (factor * value)  # calculate the correction for steering
        correction = f * factor * (value + delta)
        # correction = f * correction  # if we drive backwards negate the correction

        on(speed, correction)  # switch the steering on with the given correction and speed

        current = time.time()  # measure the crurrent time

        # if the time is used we set run to false once the end time is reached
        # if the distance is greater than the position than the leave the
        angle = left_motor.angle()

        traveled = angle_to_distance(angle)

        print(correction, angle, traveled)

        if t is not None and current > end_time:
            break  # leave the loopK
        if distance is not None and distance < traveled:
            break  # leave the loop

    stop()  # stop the robot


#######################################################
# Setup
#######################################################


def gotoblack(speed, port, black=10):
    """
    The robot moves to the black line while using the sensor on the given port

    :param speed: The speed
    :param port: The port 2,3,4
    :param black: The value to stop
    """
    on(speed, 0)
    while  light(port)  > black:
        pass
    stop()


def gotowhite(speed, port, white=90):
    """
    The robot moves to the white line while using the sensor on the given port

    :param speed: The speed
    :param port: The port 2,3,4
    :param white: The value to stop
    """

    on(speed, 0)
    while light(port) < white:
        pass
    stop()


#######################################################
# Setup
#######################################################
def setup():
    pass
    # beep()
    # sound()


    # led(None, "RED")
    # led(None, "GREEN")
    # led(None, "YELLOW")
    # flash()

    # clear()
    # Print("Hallo")
    # Print("World")
    # voltage()



    forward(25, 10)
    #time.sleep(1)
    turn(25, 45)
    #time.sleep(1)
    forward(25, 30)
    #time.sleep(1)


    turn(25, -50)
    #time.sleep(1)
    forward(25,10)
    #time.sleep(1)

    # gotowhite(25, 3)
    # gotoblack(10, 3)
    # gotowhite(10, 3)
    #forward(5, 2)
    #forward(-20, 20)

    # turn(20, 45)
    # forward(-75, 60)
    # sleep(2)

    #followline(speed=20, distance=30)