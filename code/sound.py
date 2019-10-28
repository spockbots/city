#! /usr/bin/env micropython

import spockbots.robot as robot

#robot.wav("3-5_live_long2.wav")

robot.speak('Spockbots')

robot.sing((
    ('D4', 'e3'),
    ('D4', 'e3'),
    ('D4', 'e3'),
    ('G4', 'h'),
    ('D5', 'h')
))

