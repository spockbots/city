#!/usr/bin/env pybricks-micropython
from spockbots.motor import SpockbotsMotor
import time
from spockbots.output import led, PRINT

from spockbots.gyro import SpockbotsGyro as Gyro



from spockbots.output import PRINT

"""GYRO-ANG GYRO-RATE GYRO-FAS GYRO-G&A GYRO-CAL TILT-RATE TILT-ANG"""



def run_swing():
    """
    TBD
    """



    robot = SpockbotsMotor()
    robot.debug = True

    robot.setup()
    robot.color.read()

    print(robot)

    #
    # setup gyro
    #
    gyro = Gyro(robot)
    # gyro.connect()
    gyro.reset()
    if gyro.still():
        PRINT("ROBOT STILL")
    else:
        PRINT("ROBOT DRIFT")
        led("RED")
        robot.beep()
        robot.beep()
        robot.beep()

    dt = 1.0

    def wait():
        time.sleep(dt)
        robot.beep()

    # PUT IN COLOR CALIBRATE VALUES

    robot.forward(20, 33)
    #wait()

    robot.turntowhite(25, direction="right", port=3)
    #robot.turntoblack(25, direction="right", port=3)

    #robot.turn (50, 20)  # just robot: -5  just attachment: -20 speed 50  attachment with blocks: ??
    #wait()

    robot.followline(speed=10,
                     distance=72,
                     port=3,
                     right=False,
                     black=15,
                     white=85,
                     delta=-35,
                     factor=0.4)
    # for some reason right=True is left side of line
    #wait()

    robot.forward(25, 3)

    gyro.turn(26, -10)

    robot.turntoblack(25, direction="right", port=3)


    robot.followline(speed=10,
                     distance=25,
                     port=3,
                     right=False,
                     black=15,
                     white=85,
                     delta=-35,
                     factor=0.4)

    robot.forward(25, 4)
    robot.forward(25, 5)
    gyro.turn(10, 50)

    robot.forward(10, -45)
    gyro.turn(40, 90)

    robot.forward(90, 140)


    #wait()
    """

    robot.forward(25, 15)
    wait()


    #robot.turn(25, 10)
    wait()


    time.sleep(1.0)
    """

if __name__ == "__main__":
    run_swing()