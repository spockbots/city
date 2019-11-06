#!/usr/bin/env python3

import spockbots.robot as robot
from old.run import run_test1
from old.run import run_test2
from old.run import run_calibrate


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

#test
