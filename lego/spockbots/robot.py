#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

from pybricks.parameters import Button, Color
from time import sleep

# ImageFile, SoundFile

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

def led(group, color):
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

#######################################################
# Voltage
#######################################################

def voltage():
    voltage = brick.battery.voltage() / 1000
    Print("Voltage: " + str(voltage) + " V", 10, 20)

#######################################################
# Setup
#######################################################
def setup():
    # beep()
    # sound()
    led(None, "RED")
    led(None, "GREEN")
    led(None, "YELLOW")
    flash()

    clear()
    Print("Hallo")
    Print("World")
    voltage()

    sleep(2)
