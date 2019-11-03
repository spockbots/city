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


diameter = 62.4  # mm
width = 20.0  # mm
circumference = (diameter / 10.0) * math.pi   # as diameter is in mm but we like cm

axle_track = 8 * 14

#######################################################
# Color Sensor
#######################################################


colorsensor = ColorSensor(Port.S3)

def light(port):
    return colorsensor.reflection()

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
# Motor
#######################################################


#left_motor = Motor(Port.A, direction=Direction.CLOCKWISE)
#right_motor = Motor(Port.B, direction=Direction.CLOCKWISE)

left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)

tank = DriveBase(left_motor, right_motor, diameter, axle_track)


def distance_to_rotation(distance):
    """
    calculation to convert the distance from
    cm into rotations.

    :param distance:  The distance in cm
    :return: The rotations to be traveled for the given distance
    """
    rotation = distance / circumference
    return rotation

def distance_to_angle(distance):
    """
    calculation to convert the distance from
    cm into rotations.

    :param distance:  The distance in cm
    :return: The rotations to be traveled for the given distance
    """
    rotation = distance_to_rotation(distance) * 360.0
    return rotation

def angle_to_distance(angle):
    d = circumference / 360.0 * angle
    print("A to D", angle, d)
    return d

def on(speed, steering=0):
    tank.drive(speed * 10, steering)


def stop(brake=None):
    """
    stops all motors on all different drive modes

    :param brake: None, brake, coast, hold
    :return:
    """
    """

    """
    # motor_left.stop()
    # motor_right.stop()
    if not brake or brake == "brake":
        tank.stop(stop_type=Stop.BRAKE)
    elif brake == "coast":
        tank.stop(stop_type=Stop.COAST)
    elif brake == "hold":
        tank.stop(stop_type=Stop.HOLD)


def forward(speed, distance, brake=None):
    left_motor.reset_angle(0)
    angle = distance_to_angle(distance)
    on(speed)
    while left_motor.angle() < angle:
        pass
    stop(brake=brake)

def reset_motors():
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)

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

    left_motor.run_angle(speed * 10, a, Stop.BRAKE, False)
    right_motor.run_angle(speed * 10, -a, Stop.BRAKE, False)

    while abs(left_motor.angle()) < abs(a) and abs(left_motor.angle()) < abs(a):
        pass


#######################################################
# Line
#######################################################

def followline(
        speed=25,  # speed 0 - 100
        t=None,  # time in seconds
        distance=None,  # distance in cm
        port=3,  # the port number we use to follow the line
        black=0,  # minimal balck
        white=100,  # maximal white
        delta=-35,  # paramaters to control smoothness
        factor=0.7):  # parameters to control smoothness

    print (distance)

    current = time.time()  # the current time
    if t is not None:
        end_time = current + t  # the end time

    reset_motors()

    while True:
        value = light(port)  # get the light value

        # correction = delta + (factor * value)  # calculate the correction for steering
        correction = - factor * (value + delta)
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
def setup():
    # beep()
    # sound()


    """
    font(32)
    led(None, "RED")
    led(None, "GREEN")
    led(None, "YELLOW")
    flash()

    clear()
    Print("Hallo")
    Print("World")
    voltage()

    forward(20, 30)
    forward(20, 30)
    turn(25, 90)
    forward(20, 30)
    turn(25, 10)
    forward(20, 30)
    forward(20, 30)

    sleep(2)
    """
    followline(speed=20, distance=30)