from ev3dev2.motor import OUTPUT_A, OUTPUT_B,OUTPUT_C, OUTPUT_D
from ev3dev2.motor import MoveTank, SpeedPercent, LargeMotor, MoveSteering, MediumMotor
from ev3dev2.sound import Sound
from ev3dev2.led import Leds
from ev3dev2.button import Button
from ev3dev2.sensor import INPUT_1,INPUT_2,INPUT_3,INPUT_4
from ev3dev2.sensor.lego import GyroSensor
import time
import math
from ev3dev2.wheel import Wheel
from spockbots.colorsensor import SpockbotsColorSensors

from ev3dev2.sound import Sound


# Wheel https://www.bricklink.com/v2/catalog/catalogitem.page?P=86652c01#T=C
diameter=62.4 # mm
width=20      # mm
tire = Wheel(diameter, 20) # width is 20mm

sound = Sound()
leds = Leds()

tank = MoveTank(OUTPUT_B, OUTPUT_A)
tank.left_motor.polarity='inversed'
tank.right_motor.polarity='inversed'


motor_left = LargeMotor(OUTPUT_B)
motor_right = LargeMotor(OUTPUT_A)

mediummotor_left = MediumMotor(OUTPUT_D)
mediummotor_right = MediumMotor(OUTPUT_C)


steering = MoveSteering(OUTPUT_B, OUTPUT_A)

colorsensors = SpockbotsColorSensors()

ev3gyro = GyroSensor(INPUT_1)


class Gyro(object):
    # The following link gives some hine why it does not work fo rthe Gyror in mindstorm
    # http://ev3lessons.com/en/ProgrammingLessons/advanced/Gyro.pdf

    # in python we have three issues

    # value is not 0 after reset
    # value drifts after reset as it takes time to settle down
    # value is not returened as no value is available

    # This code fixes it.

    def __init__(self, gyro):
        self.gyro = gyro
        self.last_angle = -1000
        self.gyro.mode = 'GYRO-ANG'

    def angle(self):
        try:
            self.last_angle = a = self.gyro.angle
        except:
            print("Gyro read error")
            a = self.last_angle
        return a

    def reset(self):

        self.gyro.reset()
        angle = self.gyro.angle

        count = 10
        while count >= 0:
            time.sleep(0.1)
            try:
                angle = self.gyro.angle
            except:
                print("Gyro read error")
            print(count, "Gyro Angle: ", angle)
            if angle == 0:
                count = count - 1
        self.last_angle = angle
        print("Gyro Angle, final: ", angle)


gyro = Gyro(ev3gyro)

ev3button = Button()

sound = Sound()

def speak(text):
    sound.speak(text)

def sing(song):
    sound.play_song(song)

def wav(source):
    sound.play_file("/home/robot/wav/" + source)

def button(which):
    # which = up, down, left, right, enter, backspace
    return ev3button.check_buttons(buttons=[which])

def button_wait(which):
    while True:
        if button(which):
            return


def direction(movement):
    """
    Sets the direction of the robot

    :param movement: either 'front' or 'back'
    :return:
    """
    if movement == 'front':
        tank.left_motor.polarity = 'inversed'
        tank.right_motor.polarity = 'inversed'
    elif movement == 'back':
        tank.left_motor.polarity = 'normal'
        tank.right_motor.polarity = 'normal'


def light(port):
    return colorsensors.value(port)

def power():
    p = Powersupply()
    print (p.max_voltage/p.measured_voltage)
    return p.measured_voltage

def stop():
    tank.on(SpeedPercent(0), SpeedPercent(0))

def calibrate():
    colorsensors.calibrate()

def colorvalue(port):
    return colorsensor.value(port)

def read():
    colorsensors.read()

def gotoblack(speed, port, black=10):
    """
    The robot moves to the black line while using the sensor on the given port
    """
    tank.on(SpeedPercent(speed), SpeedPercent(speed))
    while (colorvalue(port) > black):
        pass
    stop()

def gotowhite(speed, sensor, white=90):
    """
    The robot moves to the black line while using the sensor on the given port
    """
    tank.on(SpeedPercent(speed), SpeedPercent(speed))
    while (colorvalue(port) < white):
        pass
    stop()



def forever():
    True

def reset_distance():
    """
    Resests the distnace measure of the motor to 0
    """
    raise NotImplementedError

def dist(cm):
    # check if the robot traveled the distance 
    raise NotImplementedError


def followline(run=True, steering=15, speed=10, black=15, port=2):
    """
    Follows the line on a given port.
    run is a True-False function.
    If its true it continues.
    If its falls it stops

    Example:

    robot.followline_simple(robot.forever())

    """
    # this needs to be replaced with the spockbots color sensors

    while run:
        value = colorsensors.value(port)
        print (value)
        if value < black:
            tank.on(-steering, SpeedPercent(speed))
        else:
            tank.on(steering, SpeedPercent(speed))
    stop()


def followline_simple(run=True, steering=15, speed=10, black=15, port=2):
    """
    Follows the line on a given port. 
    run is a True-False function. 
    If its true it continues.
    If its falls it stops

    Example:

    robot.followline_simple(robot.forever())

    """
    # this needs to be replaced with the spockbots color sensors

    while (run):
        while colorsensors.value(port) < black:
            tank.on(SpeedPercent(speed), SpeedPercent(2*speed))
        while colorsensors.value(port) > black:
            tank.on(SpeedPercent(2*speed), SpeedPercent(speed))
    stop()

def sleep(seconds):
    """
    The robot will sleep for the number of seconds
    """
    time.sleep(seconds)

def beep():
    """
    The robot will make a beep
    """
    sound.beep()

def led(group, color):
    """
    The robot will switch on the LEDS with the given color

    group:
        LEFT
        RIGHT

    color:
        BLACK
        RED
        GREEN
        AMBER
        ORANGE
        YELLOW
    """
    # direction, LEFT
    # Color: GREEN, RED
    leds.set_color(group, color)

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
        
def distance_to_rotation(distance):
    """
    calculation to convert the distence from 
    cm into rotations.
    """
    circumference=diameter*math.pi
    rotation=distance/circumference 
    return rotation 

def forward_rotations (speed, rotations):
    """
    The robot moves forward with the given number of 
    rotations
    """
    tank.on_for_rotations(speed,speed,rotations)

def left (speed,rotations):
    """
    The robot truns left with the number of rotations
    """
    tank.on_for_rotations(speed,-speed,rotations)

def left_degrees (speed,degrees):
    """
    The robot turns left with the given number of degrees
    """
    tank.on_for_degrees(speed,-speed,degrees)

def right (speed,rotations):
    """
    The robot turns right with the number of rotations
    """
    tank.on_for_rotations(-speed,speed,rotations)

def right_degrees (speed,degrees):
    """
    The robot turns left with the given number of degrees
    """
    tank.on_for_degrees(-speed,speed,degrees)

def left_90_degrees (speed):
    """
    The robot turns left by 90 degrees
    """
    if speed==25:
        sound.speak("slow left")
        left_degrees(speed,146.5)
    elif speed==40: 
        sound.speak("fast left")  
        raise NotImplementedError         

def right_90_degrees (speed):
    """
    The robot turns left by 90 degrees
    """
    if speed==25:
        sound.speak("slow right")
        right_degrees(speed,146.5)
    elif speed==40: 
        sound.speak("fast right")           
        raise NotImplementedError         

def forward(speed, distance):
    rotations=distance_to_rotation(distance)
    forward_rotations(speed, rotations)


# forward_rotations(10,1)
# left(25,146.5)
# left_90_degrees(25)
# left_90_degrees(40)
# forward(25,100)
