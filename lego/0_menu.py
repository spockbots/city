#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.parameters import Button
from pybricks.tools import wait

from old.run.crane import run_crane
from old.run import run_swing
from old.run import run_led


# brick.display.text(text)

menu = [
    [0, "Crane", 40, 10, run_crane],
    [1, "Swing", 40, 20, run_swing],
    [2, "Red Building", 40, 30, None],
    [3, "LED", 40, 40, run_led],
]

selection = 0
selections = len(menu)


def marker(line):
    y = line * 10 + 10
    brick.display.text(">>>", (10, y))

def print_menu():
    brick.display.clear()
    for line in menu:
        i = line[0]
        text = line[1]
        x = line[2]
        y = line[3]
        brick.display.text(text, (x, y))
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

print(selection)

brick.sound.beep()

