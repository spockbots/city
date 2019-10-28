from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.sensor import INPUT_1
from ev3dev2.motor import MoveSteering, MoveDifferential
from ev3dev2.motor import SpeedPercent

# DEFINE OUR OWN TIRE CLASS
from spockbots.wheel import SpockbotsTire, STUD_MM

gyro_sensor = GyroSensor(INPUT_1)

# how to put it into : ? MODE_GYRO_ANG

mdiff = MoveDifferential(OUTPUT_A, OUTPUT_B, SpockbotsTire, 16 * STUD_MM)
tank = MoveSteering(OUTPUT_B, OUTPUT_A)

def reset():
    gyro_sensor.reset()

def left(speed, degrees=90):
    mdiff.odometry_start()
    mdiff.turn_to_angle(SpeedPercent(speed), degrees)

def right(speed, degrees=90):
    mdiff.odometry_start()
    mdiff.turn_to_angle(SpeedPercent(speed), -degrees)

def followline(distance,oort=INPUT_1):

    run = True
    reset()
    mdiff.odometry_start()
    while (run):
        angle = gyro_sensor.angle
        factor = -0.7
        correction_angle = factor * angle
        tank.on(correction_angle)
        distance = abs(getdistance)
    stop()
    mdiff.odometry_stop()