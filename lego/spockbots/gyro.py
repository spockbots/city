import sys
import time
from time import sleep

from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Direction
from pybricks.parameters import Port
from spockbots.output import led, PRINT, beep, sound, signal

#######################################################
# Gyro
#######################################################

class SpockbotsGyro(object):
    """
    improved gyro class
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



    def __init__(self, robot, port=1):
        """
        Initializes the Gyro Sensor

        :param robot: robot varible
        :param port: port number for gyro sensor 1,2,3,4
        :param direction: if front if we drive forward
                          otherwise backwards
        """

        self.robot = robot
        if self.robot.direction == "forward":
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
                signal()
                beep()
                if "No such sensor on Port" in str(e):
                    print()
                    print("ERROR: The Gyro Sensor is disconnected")
                    print()
                    sys.exit()

        # bug should be = 0
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
            print("Gyro",  "angle", a, "speed", s)
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
            # sleep(0.1)
            angle = self.angle()

    def still(self):
        """
        tests if robot does not move
        :return: True if robot does not move
        """
        return not self.drift()

    def drift(self):
        """
        tests if robot drifts and waits until its still

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
        tests count times if robot is still and returns if its still or drifts
        :param count: number of times tested if its still
        :return: still,drift which are true/false
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
        """

        self.sensor.reset_angle(0)
        try:
            self.last_angle = angle = self.sensor.angle()
        except:
            print("Gyro read error")
            self.last_angle = angle = -1000

        count = 10
        while count >= 0:
            # sleep(0.1)
            try:
                angle = self.sensor.angle()
            except:
                print("Gyro read error", angle)
            print(count, "Gyro Angle: ", angle)
            if abs(angle) <= 2:
                count = count - 1
        self.last_angle = angle
        print("Gyro Angle, final: ", angle)

    def setup(self):
        self.reset()
        if self.still():
            PRINT("ROBOT STILL")
            led("GREEN")
        else:
            PRINT("ROBOT DRIFT")
            led("RED")
            self.robot.beep()
            self.robot.beep()
            self.robot.beep()

    def turn(self, speed=25, degrees=90, offset=None):
        """
        uses gyro to turn positive to right negative to left. As it may turn too much, it
        will correct itself at a lower speed and turn. As the sensor is accurate to 2 degrees,
        we only do the correction if the robot is more than two degrees off.

        :param speed: speed it turns at
        :param degrees: degrees it turns
        :return:
        """

        if offset is None:
            if speed == 50:
                offset = 45
            elif speed == 25:
                offset = 17
            else:
                offset = 0

        if degrees < 0: # Turn LEFT

            self.left(speed=speed, degrees=abs(degrees), offset=offset)
            # correct if angle is wrong
            angle = self.angle()
            if abs(angle - degrees) > 2:
                if angle < degrees: # correct if angle is wrong
                    self.right(speed=5, degrees=abs(degrees - angle))
                elif angle > degrees:
                    self.left(speed=5, degrees=abs(degrees - angle))

        elif degrees > 0: # Turn RIGHT

            self.right(speed=speed, degrees=abs(degrees), offset=offset)
            # correct if angle is wrong
            angle = self.angle()
            if abs(angle - degrees) > 2:
                if angle > degrees:
                    self.left(speed=5, degrees=abs(degrees - angle))
                elif angle < degrees:
                    self.right(speed=5, degrees=abs(degrees - angle))

        angle = self.angle()
        print(angle)

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
        angle = self.angle()
        print("LEFT", angle)

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
        angle = self.angle()
        print("RIGHT", angle)


    def forward(self,
                speed=10,  # speed 0 - 100
                distance=None,  # distance in cm
                t=None,
                finish=None,
                min_speed=1,
                acceleration=2,
                port=1,  # the port number we use to follow the line
                delta=-180,  # control smoothness
                factor=0.01):  # parameters to control smoothness
        """
        Moves forward

        :param speed: The speed
        :param distance: If set the distance to travle
        :param t: If set the time to travel
        :param port: The port number of the Gyro sensor
        :param delta: controlling the smoothness of the line
        :param factor: controlling the smoothness of the line

        Examples:

        gyro.forward(50, distance=30, factor=0.005)

        """

        def forever():
            return False

        if finish == None:
            finish = forever

        print ("GGGG")

        current_speed = min_speed

        if self.robot.check_kill_button():
            return

        if distance is not None:
            distance = 10 * distance

        current = time.time()  # the current time
        if t is not None:
            end_time = current + t  # the end time

        self.robot.reset()
        self.reset()
        while not finish():
            if self.robot.check_kill_button():
                return
            value = self.angle()  # get the Gyro angle value

            # correction = delta + (factor * value)
            # calculate the correction for steering
            correction = factor * (value + delta) / 180.0 * 100.0

            self.robot.on(current_speed, correction)  # switch the steering on
                           # with the given correction and speed

            # if the time is used we set run to false once
            #        the end time is reached
            # if the distance is greater than the
            #        position than the leave the
            distance_angle = self.robot.left.angle()

            traveled = self.robot.angle_to_distance(distance_angle)

            current = time.time()  # measure the current time
            if t is not None and current > end_time:
                break  # leave the loopK
            if distance is not None and distance < traveled:
                break  # leave the loop

            # accelerate to make the robot start slowly to not effect the angle
            if current_speed < speed:
                current_speed = current_speed + acceleration

        self.robot.stop()  # stop the robot
