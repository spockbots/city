#!/usr/bin/env pybricks-micropython
""" This is the brick menu

test line

"""

from pybricks.parameters import Button
from pybricks.tools import wait

from run.crane import run_crane
from run.swing import run_swing
from run.black_circle import run_black_circle
from run.red_circle import run_red_circle
from run.tan_circle import run_tan_circle
from run.ramp import run_ramp

from run.calibrate import run_calibrate

# from run.led import run_led
# from run.check import run_check
# from run.turn_to_black import run_turn_to_black

from pybricks import ev3brick as brick

# brick.display.text(text)

# the menu contains a label and the name of the functions
# we call when we select the line with the label
menu = [
    ["Swing", run_swing],
    ["Crane", run_crane],
    ["Red Circle", run_red_circle],
    ["Tan Circle", run_tan_circle],
    ["White to Black Circle", run_black_circle],
    ["Ramp", run_ramp],
#    ["Calibrate", run_calibrate]
]

selection = 0
selections = len(menu)


def marker(line):
    """
    Place a marker in fornt of the selected line
    """
    y = line * 10 + 10
    brick.display.text(">>>", (10, y))


def print_menu():
    """
    Print the menu
    """
    brick.display.clear()
    i = 0
    for line in menu:
        text = line[0]
        x = 40
        y = i * 10 + 10
        brick.display.text(text, (x, y))
        i = i + 1
    marker(selection)


brick.sound.beep()

print_menu()

while True:
    if Button.UP in brick.buttons():
        selection = (selection - 1) % selections
        print_menu()

    elif Button.DOWN in brick.buttons():
        selection = (selection + 1) % selections
        print_menu()

    elif Button.RIGHT in brick.buttons():
        prg = menu[selection][1] # get the function name from the menu
        brick.display.clear() # clear the scree
        prg() # run the selected function
        brick.display.clear() # clear the screen as we are now done with the prg
        print_menu() # print the screen

    elif Button.LEFT in brick.buttons():
        brick.display.clear()
        break

    wait(100)

brick.display.clear()

brick.sound.beep()
