#! /usr/bin/env python

import easygui
import sys
import os
from time import time

debug = True
debug = False
base = "lego"


def run(command):
    print(command)
    if not debug:
        t_start = time()
        os.system(command)
        t_end = time()
        print ("Time:", round(t_end - t_start, 2), "s")

robot = "blue"
prg = "interpreter"
action = None
python="bybricks-micropython"


robots = ['red', 'blue']
prgs = ['interpreter']
#actions = ['Update robot.py', 'Upload', 'Run', 'Clean', 'Quit']
actions = ['Upload', 'Clean', 'Quit']

pythons=['python3', 'micropython', 'bybricks-micropython']
clean = ['clean']

choices = robots + prgs + pythons + actions
while 1:
    msg = f"Robot: {robot}\nProgram: {prg}\nPython: {python}"
    choice=easygui.buttonbox(msg, "Spockbots", choices)

    if choice in prgs:
        prg = choice
    elif choice in robots:
        robot = choice
    elif choice in actions:
        action = choice
        print(action)

        if action == 'Quit':
            sys.exit(0)
        # elif action == "Update robot.py":
        #     run(f"scp -r {base}/spockbots/robot.py {robot}:spockbots/.")
        elif action == "Clean":
            run(f"make clean")
            run(f'ssh {robot} "rm -rf run spockbots x_examples 0_menu.py"')

        elif action == "Upload":
            run(f"scp -r {base}/spockbots {base}/x_examples {base}/run {base}/*.py {robot}:.")
        elif action == "Run":
            run(f'ssh {robot} "{python} ./{prg}.py"')
        print("Action complete ...")
        os.system("say ok")
        print()
    elif choice in pythons:
        python = choice


