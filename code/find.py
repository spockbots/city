#!/usr/bin/env python3

kp = 3
ki = 0.01
kd = 0

"""
it will ask you for three values once you enter i
For each value you can do

enter: value is unchanged
+number: adds a number to the value
-number: subtracts a number to the value

if you enter r it will print run (that is where we need to call the line follower

"""

def change (kind, value):
    c = input("Add to value {}={:0.2f}: ".format(kind,value))
    if c == "":
        return value
    value = value + float(c)
    return round(value, 2)

while (True):

    c = input("Wait for i or r: ")
    if c == "i":
        kp = change("kp", kp)
        ki = change("ki", ki)
        kd = change("kd", kd)

        print()
        print("Values")
        print()
        print("kp:", kp)
        print("ki:", ki)
        print("kd:", kd)
        print()
    elif c == "r":
        print("run")




"""
import spockbots.robot as robot

robot.beep()
robot.read()

robot.colorsensors.info()




while True:
    txt = "exit"
    if robot.button('backspace'):
        break
    elif robot.button('up'):
        run_swing()
    elif robot.button('down'):
        run_tree()
    elif robot.button('left'):
        run_test1()
    elif robot.button('right'):
        run_test2()
    elif robot.button('enter'):
        run_calibrate()

print(txt)
robot.flash()
"""