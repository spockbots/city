from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.motor import follow_for_ms
from ev3dev2.motor import Motor, SpeedPercent, LargeMotor, MoveSteering, MediumMotor

from ev3dev2.motor import MoveTank
#from spockbots.motor import MoveTank

from ev3dev2.sound import Sound
from ev3dev2.led import Leds
from ev3dev2.button import Button
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import GyroSensor
import time
import math
from ev3dev2.wheel import Wheel
from spockbots.colorsensor import SpockbotsColorSensors

from ev3dev2.sound import Sound
from threading import Thread
import sys
import os

# Wheel https://www.bricklink.com/v2/catalog/catalogitem.page?P=86652c01#T=C
diameter = 6.24  # cm
width = 2.0  # cm
position_per_cm = 1.0/18.42

tire = Wheel(diameter, 20)  # width is 20mm

sound = Sound()
leds = Leds()

tank = MoveTank(OUTPUT_B, OUTPUT_A)

motor_left = LargeMotor(OUTPUT_B)
motor_right = LargeMotor(OUTPUT_A)

mediummotor_left = MediumMotor(OUTPUT_D)
mediummotor_right = MediumMotor(OUTPUT_C)

steering = MoveSteering(OUTPUT_B, OUTPUT_A)

colorsensors = SpockbotsColorSensors()

ev3gyro = GyroSensor(INPUT_1)

mediummotor_left.off()
mediummotor_right.off()

moves_forward = True

def medium_left(speed, degrees):
    mediummotor_left.on_for_rotations(speed, int(degrees/360))
    mediummotor_left.off()

def door_open(speed=50, degree=360):
    medium_left(speed, degree)

def door_closed(speed=-50, degree=360):
    medium_left(speed, degree)


class Gyro(object):
    # The following link gives some hine why it does not work fo rthe Gyror in mindstorm
    # http://ev3lessons.com/en/ProgrammingLessons/advanced/Gyro.pdf

    # in python we have three issues

    # sensor value is not 0 after reset
    # sensor value drifts after reset as it takes time to settle down
    # sensor value is not returned as no value is available from the sensor

    # This code fixes it.

    def __init__(self, gyro):
        """
        Initializes the Gyro Sensor
        :param gyro: The gyro sensor on a given port
        """
        self.gyro = gyro
        self.last_angle = -1000 # just set the current value to get us started
        self.gyro.mode = 'GYRO-ANG' # set the sensor in angle mode

    def angle(self):
        """
        Gets the angle

        :return: The angle in degrees
        """
        try:
            self.last_angle = a = self.gyro.angle
        except:
            print("Gyro read error")
            a = self.last_angle
        return a

    def zero(self):
        self.gyro.reset()
        time.sleep(0.2)

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


###########################################################
# Buttons
###########################################################

def button(which):
    # which = up, down, left, right, enter, backspace
    return ev3button.check_buttons(buttons=[which])


def button_wait(which):
    while True:
        if button(which):
            return

def button_kill(which="backspace"):
    print("RUNNING")
    count = 0
    button_wait(which)
    print("KILL")
    os.system("micropython /home/robot/stop.py")
    sys.exit()


t = Thread(target=button_kill)
t.start()


###########################################################

def direction(movement):
    """
    Sets the direction of the robot

    :param movement: either 'front' or 'back'
    :return:
    """
    if movement == 'front':
        moves_forward = True
        tank.left_motor.polarity = 'inversed'
        tank.right_motor.polarity = 'inversed'

        steering.left_motor.polarity = 'inversed'
        steering.right_motor.polarity = 'inversed'

        motor_left.polarity = 'inversed'
        motor_right.polarity = 'inversed'


    elif movement == 'back':
        moves_forward = False
        tank.left_motor.polarity = 'normal'
        tank.right_motor.polarity = 'normal'

        steering.left_motor.polarity = 'normal'
        steering.right_motor.polarity = 'normal'

        motor_left.polarity = 'normal'
        motor_right.polarity = 'normal'


def light(port):
    """
    get the light value from the colorsensor on the port
    :param port: The port, number 2, 3, 4
    :return: The light value
    """
    return colorsensors.value(port)


def voltage():
    """
    Gets the current vultage.

    :return: The measured voltage
    """
    p = Powersupply()
    print("Voltage: ", p.max_voltage / p.measured_voltage)
    return p.measured_voltage


def kill():
    """
    stops the motors
    """
    ports = [OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D]
    for port in ports:
        motor = Motor(port)
        motor.off()


def medium_stop():
    """
    stops all medium motors
    """
    mediummotor_left.off()
    mediummotor_right.off()


def stop():
    """
    stops all motors on all different drive modes
    """
    tank.off()
    steering.off()
    motor_left.off()
    motor_right.off()
    kill()

def calibrate():
    """
    runs the calibraion for the 3 color sensors
    :return:
    """
    colorsensors.calibrate()


def colorvalue(port):
    """
    returns the color value from the given port
    :param port: The port number 2, 3, 4
    :return: the color value
    """
    return colorsensor.value(port)


def read():
    """
    reads the color values from the file that were written by calibrate
    :return:
    """
    colorsensors.read()


def gotoblack(speed, port, black=10):
    """
    The robot moves to the black line while using the sensor on the given port

    :param speed: The speed
    :param port: The port 2,3,4
    :param black: The value to stop
    """
    tank.on(SpeedPercent(speed), SpeedPercent(speed))
    while colorvalue(port) > black:
        pass
    stop()


def gotowhite(speed, sensor, white=90):
    """
    The robot moves to the white line while using the sensor on the given port

    :param speed: The speed
    :param port: The port 2,3,4
    :param white: The value to stop
    """
    tank.on(SpeedPercent(speed), SpeedPercent(speed))
    while colorvalue(port) < white:
        pass
    stop()

def reset_distance():
    """
    Resests the distnace measure of the motor to 0
    """
    raise NotImplementedError


def dist(cm):
    # check if the robot traveled the distance 
    raise NotImplementedError


def followline(
        speed=25,  # speed 0 - 100
        t=None,  # time in seconds
        distance=None,  # distance in cm
        port=3,  # the port number we use to follow the line
        black=0,  # minimal balck
        white=100,  # maximal white
        delta=-35,  # paramaters to control smoothness
        factor=0.7):  # parameters to control smoothness

    global moves_forward  # taken from the direction function
    if moves_forward:  # set to + if forward and - if backward
        f = 1.0
    else:
        f = -1.0

    current = time.time()  # the current time
    if t is not None:
        end_time = current + t  # the end time

    steering.left_motor.position = 0  # set the motor position to 0
    # 1.842 positions is 1cm

    while True:
        value = light(port)  # get the light value

        correction = delta + (factor * value)  # calculate the correction for steering
        correction = f * correction  # if we drive backwards negate the correction

        print(correction)

        steering.on(correction, speed)  # switch the steering on with the given correction and speed

        current = time.time()  # measure the crurrent time

        # if the time is used we set run to false once the end time is reached
        # if the distance is greater than the position than the leave the
        if t is not None and current > end_time:
            break  # leave the loop
        if distance is not None and distance > position_per_cm * steering.left_motor.position:
            break  # leave the loop

    steering.off()  # stop the robot


def sleep(seconds):
    """
    The robot will sleep for the number of seconds

    :param seconds: number of seconds
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
    calculation to convert the distance from
    cm into rotations.

    :param distance:  The distance in cm
    :return: The rotations to be traveled for the given distance
    """
    circumference = diameter * math.pi
    rotation = distance / circumference
    return rotation


def forward_rotations(speed, rotations):
    """
    drive forward for the given rotations

    :param speed: the speed
    :param rotations: the rotations
    :return:
    """
    left_start = motor_left.position
    right_start = motor_right.position

    tank.on_for_rotations(speed, speed, rotations)

    left_end = motor_left.position
    right_end = motor_right.position

    tank.wait_while('running', timeout=3000)
    tank.off()

    print("Distance Position", left_end - left_start, right_end - right_start)


def left_rotations(speed, rotations):
    """
    drive to the left for the given rotations

    :param speed: The speed
    :param rotations: The rotations
    """
    tank.on_for_rotations(-speed, speed, rotations)
    tank.off()


def right_rotations(speed, rotations):
    """
    drive to the right for the given rotations

    :param speed: The speed
    :param rotations: The rotations
    """
    tank.on_for_rotations(speed, -speed, rotations)
    tank.off()

def left(speed=25, degrees=90, offset=0):
    """
    The robot turns left with the given number of degrees

    :param speed: The speed
    :param degrees: The degrees
    """
    if speed == 25:
        offset = 5

    gyro.zero()

    tank.on(-speed, speed)
    while gyro.angle() > -degrees + offset:
        pass
    #tank.on_for_degrees(speed, -speed, degrees)
    tank.off()


def right(speed=25, degrees=90, offset=0):
    """
    The robot turns left with the given number of degrees

    :param speed: The speed
    :param degrees: The degrees
    """
    if speed == 25:
        offset = 5

    gyro.zero()
    tank.on(speed, -speed)
    while gyro.angle() < degrees - offset:
        pass
#
    #tank.on_for_degrees(speed, -speed, degrees)
    tank.off()

def forward(speed, distance):
    """

    Go forward

    :param speed: The speed of the robot
    :param distance: distance in cm
    :return:
    """
    rotations = distance_to_rotation(distance)
    forward_rotations(speed, rotations)

def check():
    """
    do a robot check by

    a) turning on the large motors one at a time
    b) turning on the medium motors one at a time
    c) turning on the light sensors one at a time
    """
    beep()

    speak('Large Motors')

    speak('Left')
    motor_left.on_for_seconds(25, 1)

    speak('Right')
    motor_right.on_for_seconds(25, 1)

    speak('Medium Motors')

    speak('Left')
    mediummotor_left.on_for_seconds(25, 1)

    speak('Right')
    mediummotor_right.on_for_seconds(25, 1)

    speak('Light')

    speak('Left')
    colorsensors.flash(ports=[2])

    speak('Right')
    colorsensors.flash(ports=[3])

    speak('Back')
    colorsensors.flash(ports=[4])

    speak('finished')


# forward_rotations(10,1)
# left(25,146.5)
# left_90_degrees(25)
# left_90_degrees(40)
# forward(25,100)

direction('front') # set the defualt direction to move to the front so we do not forget.
