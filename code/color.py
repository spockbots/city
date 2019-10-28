#!/usr/bin/env python3

import spockbots.robot as robot


from spockbots.colorsensor import SpockbotsColorSensor


for port in [2,3,4]:
    color = SpockbotsColorSensor(2)
    color.flash()



