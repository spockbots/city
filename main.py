#!/usr/bin/env micropython

import spockbots.robot as robot
from run.test1 import run_test1
from run.test2 import run_test2
from run.calibrate import run_calibrate


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
