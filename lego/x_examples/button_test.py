#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import Button



#print('LEFT_DOWN', str(Button.LEFT_DOWN))
#print('DOWN', str(Button.DOWN))
#print('RIGHT_DOWN', str(Button.RIGHT_DOWN))
#print('LEFT', str(Button.LEFT))
#print('CENTER', str(Button.CENTER))
#print('RIGHT', str(Button.RIGHT))
#print('LEFT_UP', str(Button.LEFT_UP))
#print('UP', str(Button.UP))
#print('BEACON', str(Button.BEACON))
#print('RIGHT_UP', str(Button.RIGHT_UP))

"""
>>> from pybricks.parameters import Button
>>> help (Button)
object <class ''> is of type type
  UP -- 256
  DOWN -- 4
  LEFT -- 16
  RIGHT -- 64
  CENTER -- 32
  LEFT_UP -- 128
  LEFT_DOWN -- 2
  RIGHT_UP -- 512
  RIGHT_DOWN -- 8
  BEACON -- 256
  
"""

while True:
    b = brick.buttons()
    if b != []:
        print(b)

backspace = 128
up = 256
down = 4
left = 16
right = 64
center = 32