import sys
import time
from time import sleep

from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Direction
from pybricks.parameters import Port


#######################################################
# Gyro
#######################################################

class SpockbotsGyro(object):
    """
    test
    """
    # The following link gives some hints why it does not
    # work for the Gyro in mindstorm
    # http://ev3lessons.com/en/ProgrammingLessons/advanced/Gyro.pdf

    # in python we have three issues

    # sensor value is not 0 after reset
    # sensor value drifts after reset as it takes time
    #        to settle down
    # sensor value is not returned as no value is available
    #        from the sensor

    # This code fixes it.

    def __init__(self, robot, port=1, direction="front"):
        """
        Initializes the Gyro Sensor
        :param gyro: The gyro sensor on a given port
        """

        self.robot = robot
        if direction == "front":
            sensor_direction = Direction.CLOCKWISE
        else:
            sensor_direction = Direction.COUNTERCLOCKWISE

        found = False
        while not found:
            print("FINDING GYRO")
            try:
                if port == 1:
                    self.sensor = GyroSensor(Port.S1,
                                             sensor_direction)
                elif port == 2:
                    self.sensor = GyroSensor(Port.S2,
                                             sensor_direction)
                elif port == 3:
                    self.sensor = GyroSensor(Port.S3,
                                             sensor_direction)
                elif port == 4:
                    self.sensor = GyroSensor(Port.S4,
                                             sensor_direction)
                print("SENSOR:", self.sensor)
                sleep(0.1)
                self.sensor.reset_angle(0)
                found = True
            except Exception as e:
                print(e)
                if "No such sensor on Port" in str(e):
                    print()
                    print("ERROR: THe Gyro Sensor is disconnected")
                    print()
                    sys.exit()

        self.last_angle = -1000  # just set the current value
                                 # to get us started
        print("GYRO INITIALIZED")

    def angle(self):
        """
        Gets the angle

        :return: The angle in degrees
        """
        try:
            s = self.sensor.speed()
            a = self.sensor.angle()
            print("AS", a, s)
            self.last_angle = a
        except:
            print("Gyro read error")
            a = self.last_angle

        return a

    def zero(self):
        """
        set the gyro angle to 0
        :return:
        """
        self.sensor.reset_angle(0)

        angle = 1000
        while angle != 0:
            sleep(0.1)
            angle = self.angle()

    def still(self):
        """

        :return:
        """
        return not self.drift()

    def drift(self):
        """

        :return:
        """
        # loop in case we get a read error from the gyro speed
        while True:
            try:
                speed = self.sensor.speed()
                if speed == 0:
                    return False  # no drift if the speed is 0
                else:
                    return True  # DRIFT IF THE SPEED IS NOT 0
            except:
                print("ERROR: DRIFT no value found")
                # No speed value found, so repeat

    def status(self, count=10):
        """

        :param count:
        :return:
        """
        last = self.angle()
        i = 0
        still = 0
        drift = 0
        while i <= count:
            angle = self.angle()
            if angle == last:
                still = still + 1
                drift = 0
            else:
                drift = drift + 1
            i = i + 1
        print("GYRO STATUS", i, still, drift)
        return still >= count, drift >= count

    def reset(self):
        """
        safely resets the gyro
        :return:
        """

        self.sensor.reset_angle(0)
        try:
            self.last_angle = angle = self.sensor.angle()
        except:
            print("Gyro read error")
            self.last_angle = angle = -1000

        count = 10
        while count >= 0:
            sleep(0.1)
            try:
                angle = self.sensor.angle()
            except:
                print("Gyro read error", angle)
            print(count, "Gyro Angle: ", angle)
            if abs(angle) <= 2:
                count = count - 1
        self.last_angle = angle
        print("Gyro Angle, final: ", angle)

    def turn(self, speed=25, degrees=90):
        """

        :param speed:
        :param degrees:
        :return:
        """
        if degrees < 0:
            self.left(speed=speed, degrees=abs(degrees))
        elif degrees > 0:
            self.right(speed=speed, degrees=abs(degrees))

    def left(self, speed=25, degrees=90, offset=0):
        """
        The robot turns left with the given number of degrees

        :param speed: The speed
        :param degrees: The degrees
        :param offset:
        :return:
        """
        self.reset()
        if speed == 25:
            offset = 8

        # self.zero()

        self.robot.on_forever(speed, -speed)
        angle = self.angle()

        print(angle, -degrees + offset)

        while angle > -degrees + offset:
            # print(angle, -degrees + offset)
            angle = self.angle()
        self.robot.stop()

    def right(self, speed=25, degrees=90, offset=0):
        """
        The robot turns right with the given number of degrees

        :param speed: The speed
        :param degrees: The degrees
        :param offset:
        :return:
        """
        self.reset()

        if speed == 25:
            offset = 8

        # self.zero()

        self.robot.on_forever(-speed, speed)
        angle = self.angle()
        print(angle, degrees - offset)
        while angle < degrees - offset:
            # print(angle, degrees - offset)
            angle = self.angle()
        self.robot.stop()


    def forward(self,
                speed=25,  # speed 0 - 100
                distance=None,  # distance in cm
                t=None,
                port=3,  # the port number we use to follow the line
                delta=-35,  # control smoothness
                factor=0.7):  # parameters to control smoothness
        """

        :param speed:
        :param distance:
        :param t:
        :param port:
        :param right:
        :param black:
        :param white:
        :param delta:
        :param factor:
        :return:
        """

        if right:
            f = 1.0
        else:
            f = - 1.0

        if distance is not None:
            distance = 10 * distance

        current = time.time()  # the current time
        if t is not None:
            end_time = current + t  # the end time

        self.reset()

        while True:
            value = self.angle()  # get the Gyro angle value

            # correction = delta + (factor * value)
            # calculate the correction for steering
            correction = f * factor * (value + delta)

            self.on(speed, correction)  # switch the steering on
                           # with the given correction and speed

            # if the time is used we set run to false once
            #        the end time is reached
            # if the distance is greater than the
            #        position than the leave the
            distance_angle = self.left.angle()

            traveled = self.angle_to_distance(distance_angle)

            current = time.time()  # measure the current time
            if t is not None and current > end_time:
                break  # leave the loopK
            if distance is not None and distance < traveled:
                break  # leave the loop

        self.stop()  # stop the robot
