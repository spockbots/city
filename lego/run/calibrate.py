from spockbots.motor import SpockbotsMotor
import time


def run_calibrate():
    """
    Run the calibration

    :return: a file called calibrate.txt that contains the minimum black and the
             aximum white value for the sensors
    """
    robot = SpockbotsMotor()
    robot.debug = True

    robot.setup()

    print(robot)

    robot.beep()
    robot.calibrate(10, distance=30, ports=[2, 3, 4], direction='front')
    robot.beep()

    # robot.forward(25,10)

    # robot.calibrate(10, ports=[4], direction='back')

    robot.colorsensors.write()

    time.sleep(0.5)


if __name__ == "__main__":
    time_start = time.time()
    run_calibrate()
    time_end = time.time()
    print("Time:", time_end - time_start)
