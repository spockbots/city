#! /usr/bin/env python

import easygui
import sys
import os
from time import time

debug = True
debug = False

def run(command):
    print(command)
    if not debug:
        t_start = time()
        os.system(command)
        t_end = time()
        print ("Time:", t_end - t_start)

robot = "red"
prg = "interpreter"
action = None
python="python3"


robots = ['red', 'blue']
prgs = ['interpreter']
actions = ['Upload', 'Update robot.py', 'Run', 'Quit']
pythons=['python3', 'micropython']


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
        elif action == "Update robot.py":
            run(f"scp -r code/spockbots/robot.py {robot}:spockbots/.")
        elif action == "Upload":
            run(f"scp -r code/spockbots code/*.py {robot}:.")
        elif action == "Run":
            run(f'ssh {robot} "{python} ./{prg}.py"')

        print("Action complete ...")
        os.system("say ok")
        print()

    elif choice in pythons:
        python = choice


