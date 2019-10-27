#! /usr/bin/env micropython

# Simple program to just turn off all the motors

from ev3dev2.motor import Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D

motorlist = [OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D]
for motorport in motorlist:
    motor = Motor(motorport)
    motor.off()
    del motor

