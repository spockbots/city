from spockbots.motor import SpockbotsMotor
from spockbots.output import PRINT, led


def check(speed=100, angle=360):
    """
    do a robot check by

    a) turning on the large motors one at a time
    b) turning on the medium motors one at a time
    c) turning on the light sensors one at a time

    :param speed:
    :param angle:
    :return:
    """
    robot = SpockbotsMotor()
    robot.debug = True

    robot.setup()

    speed = speed * 10

    print(robot)

    robot.beep()

    PRINT('Light')

    PRINT('Left')
    led("RED")
    robot.colorsensor[2].flash()

    PRINT('Right')
    led("GREEN")
    robot.colorsensor[3].flash()

    PRINT('Back')
    led("YELLOW")
    robot.colorsensor[4].flash()

    led("GREEN")

    PRINT('Large Motors')

    PRINT('Left')
    led("RED")
    robot.left.run_angle(speed, angle)

    PRINT('Right')
    led("GREEN")

    robot.right.run_angle(speed, angle)

    PRINT('Medium Motors')

    PRINT('Left')
    led("RED")
    robot.left_medium.run_angle(speed, angle)

    PRINT('Right')
    led("GREEN")
    robot.right_medium.run_angle(speed, angle)

    PRINT('finished')
