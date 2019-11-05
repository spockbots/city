#!/usr/bin/env pybricks-micropython
# from pybricks import ev3brick as brick
from time import sleep
from pybricks.parameters import Button
from pybricks.tools import wait

# brick.display.text(text)

menu = [
    [0, "Crane", 40, 10],
    [1, "Swing", 40, 20],
    [2, "Red Building", 40, 30]
]



brick.sound.beep()

selection = 0
selections = len(menu)

while True:
    brick.display.clear()

    for line in menu:
        i = line[0]
        text = line[1]
        x = line[2]
        y = line[3]
        brick.display.text(text, (x, y))

    # marker

    if Button.UP in brick.buttons():
        # print ("UP", selection)
        selection = (selection - 1) % selections
    elif Button.DOWN in brick.buttons():
        # print ("DOWN", selection)
        selection = (selection + 1) % selections
    elif Button.RIGHT in brick.buttons():
        break
    brick.display.text(">>>", (10, selection * 10 + 10))

    wait(100)

print(selection)

brick.sound.beep()
brick.display.clear()

