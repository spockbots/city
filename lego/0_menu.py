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

menu = [
    ["Crane", run_crane],
    ["Swing", run_swing],
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

    :param line:
    :return:
    """
    y = line * 10 + 10
    brick.display.text(">>>", (10, y))


def print_menu():
    """

    :return:
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
        prg = menu[selection][1]
        brick.display.clear()
        prg()
        brick.display.clear()
        print_menu()

    elif Button.LEFT in brick.buttons():
        brick.display.clear()
        break

    wait(100)

brick.display.clear()

brick.sound.beep()
