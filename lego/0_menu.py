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

from run.led import run_led
from run.calibrate import run_calibrate
from run.check import run_check
from run.turn_to_black import run_turn_to_black

from pybricks import ev3brick as brick

# brick.display.text(text)

menu = [
    ["Crane", run_crane],
    ["Swing", run_swing],
    ["Red Building", run_red_building],
    ["Tan Building", run_tan_building],
    ["Black/White Building", run_black_building],
    ["LED", run_led],
    ["Turn to black", run_turn_to_black]
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
        prg = menu[selection][4]
        prg()

    elif Button.LEFT in brick.buttons():
        break

    wait(100)

brick.display.clear()

brick.sound.beep()
