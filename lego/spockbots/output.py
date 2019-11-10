#!/usr/bin/env pybricks-micropython

import os
from time import sleep

from pybricks import ev3brick as brick
from pybricks.parameters import Color

#######################################################
# READ AND WRITE FILES
#######################################################

debug = True

#######################################################
# READ AND WRITE FILES
#######################################################

def readfile(name):
    """
    Reads the file with the name and returns it as a string.

    :param name: The file name
    :return: The data in teh file as string
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
    Writes a new file with the name. If it exists the
    old file will be deleted.

    :param name: The name of the file
    :param msg: The message to be placed in the file
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

def beep():
    """
    The robot will make a beep
    """
    brick.sound.beep()


def sound(pitch=1500, duration=300):
    """
    plays a sound

    :param pitch: sound pitch
    :param duration: how long the sound plays
    :return:
    """
    brick.sound.beep(pitch, duration)


#######################################################
# LED
#######################################################

def led(color):
    """
    changes color of led light

    :param color: light color
    :param brightness: light brightness
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


def flash(colors=["RED", "BLACK", "RED", "BLACK", "GREEN"],
          delay=0.1):
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
    clears display

    """
    brick.display.clear()


def PRINT(*args, x=None, y=None):
    """
    prints message on screen at x and y and on the console.
    if x and y are missing prints on next position on lcd screen
    this message prints test messages.

    The sceensize is maximum x=177, y=127)

    :param args: multible strings to be printed in between them
    :param x: x value
    :param y: y value
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
    prints voltage of battery
    """
    value = brick.battery.voltage() / 1000
    PRINT("Voltage: " + str(value) + " V", 80, 10)
