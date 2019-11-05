#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import Button
from pybricks.parameters import Color
from time import sleep

import os

#######################################################
# READ AND WRITE FILES
#######################################################

def readfile(name):
    try:
        # print ("READ", name)
        f = open(name)
        data = f.read().strip()
        f.close()
        return data
    except:
        return None

def writefile(name, msg):
    #print ("WRITE", name, msg)
    #f = open(name)
    #.write(msg)
    #f.close()
    command = "echo " + msg + " > " + name
    command = command.replace("&", "\&")
    command = command.replace(":", "\:")
    print(command)
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
    brick.display.clear()


def PRINT(text, x=None, y=None):
    if x is not None and y is not None:
        brick.display.text(text, (x, y))
    else:
        brick.display.text(text)
        print(text)

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
    value = brick.battery.voltage() / 1000
    Print("Voltage: " + str(value) + " V", 10, 20)

