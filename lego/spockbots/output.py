#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import Button
from pybricks.parameters import Color
from time import sleep

import os

#######################################################
# READ AND WRITE FILES
#######################################################

debug = True

#######################################################
# READ AND WRITE FILES
#######################################################

def readfile(name):
    """

    :param name:
    :return:
    """
    try:
        # print ("READ", name)
        f = open(name)
        data = f.read().strip()
        f.close()
        return data
    except:
        return None


def writefile(name, msg):
    """

    :param name:
    :param msg:
    :return:
    """
    # print ("WRITE", name, msg)
    # try:
    #    f = open(name)
    #    f.write(msg)
    #    f.close()
    # except Exception as e:
    #    print("FILE WRITE ERROR")
    #    print(e)

    command = 'echo \"' + msg + '\" > ' + name
    # print("COMMNAD:", command)
    os.system(command)


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

def led(color, brightness=255):
    """

    :param color:
    :param brightness:
    :return:
    """
    if color == "RED":
        led_color = Color.RED
    elif color == "GREEN":
        led_color = Color.GREEN
    elif color == "YELLOW":
        led_color = Color.YELLOW
    elif color == "BLACK":
        led_color = Color.BLACK
    elif color == "ORANGE":
        led_color = Color.ORANGE
    else:
        led_color = None
    brick.light(led_color)


def flash(colors=["RED", "BLACK", "RED", "BLACK", "GREEN"], delay=0.1):
    """
    The robot will flash the LEDs and beep twice
    """
    beep()
    for color in colors:
        led(color)
        sleep(delay)
    beep()


#######################################################
# LCD
#######################################################

def clear():
    """

    :return:
    """
    brick.display.clear()


#
# BUG THERE IS SOMEWHERE ANOTHER PRINT
#
def PRINT(*args, x=None, y=None):
    """

    :param args:
    :param x:
    :param y:
    :return:
    """
    text = ""
    for a in args:
        if a is not None:
            text = text + str(a) + " "
    if x is not None and y is not None:
        brick.display.text(text, (x, y))
    else:
        brick.display.text(text)
        print(text)


#######################################################
# Voltage
#######################################################

def voltage():
    """

    :return:
    """
    value = brick.battery.voltage() / 1000
    PRINT("Voltage: " + str(value) + " V", 80, 10)
