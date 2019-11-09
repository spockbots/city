import math
import time

from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.parameters import Stop, Direction
from pybricks.robotics import DriveBase
# from pybricks.ev3devices import ColorSensor
# from spockbots.colorsensor import SpockbotsColorSensor
from spockbots.colorsensor import SpockbotsColorSensors
from spockbots.output import debug
from spockbots.output import PRINT


#######################################################
# Motor
#######################################################


class SpockbotsMotor(object):

    def __init__(self, direction=None):
        """

        :param direction:
        """

        self.diameter = round(62.4, 3)  # mm
        self.width = 20.0  # mm
        self.circumference = round(self.diameter * math.pi, 3)  # as diameter is in mm
        # self.axle_track = round(8.0 * 14, 3)
        self.axle_track = 140.0
        self.direction = "forward"

        self.left, self.right, self.tank = self.setup(direction=direction)

        self.color = SpockbotsColorSensors(ports=[2, 3, 4])
        self.colorsensor = [None, None, None, None, None]

        for port in [2, 3, 4]:
            self.colorsensor[port] = self.color.colorsensor[port]

    def beep(self):
        """
        The robot will make a beep
        """
        brick.sound.beep()

    def __str__(self):
        PRINT()
        PRINT("Robot Info")
        PRINT("============================")
        PRINT("Tire Diameter:", self.diameter)
        PRINT("Circumference:", self.circumference)
        PRINT("Tire Width:   ", self.width)
        PRINT("Axle Track:   ", self.axle_track)
        PRINT("Angle Left:   ", self.left.angle())
        PRINT("Angle Right:  ", self.right.angle())
        PRINT("Direction:    ", self.direction)

        PRINT()

    def setup(self, direction=None):
        """

        :param direction:
        :return:
        """

        if direction is None:
            self.direction = "forward"
        else:
            self.direction = direction

        if self.direction == "forward":

            self.left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
            self.right = Motor(Port.B, Direction.COUNTERCLOCKWISE)
        else:
            self.left = Motor(Port.A, Direction.CLOCKWISE)
            self.right = Motor(Port.B, Direction.CLOCKWISE)

        self.tank = DriveBase(self.left, self.right, self.diameter, self.axle_track)

        self.left_medium = Motor(Port.D, Direction.CLOCKWISE)
        self.right_medium = Motor(Port.C, Direction.CLOCKWISE)

        return self.left, self.right, self.tank

    def light(self, port):
        """

        :param port:
        :return:
        """
        return self.colorsensor[port].light()

    def reset(self):
        """

        :return:
        """
        self.left.reset_angle(0)
        self.right.reset_angle(0)

    def on(self, speed, steering=0):
        """

        :param speed:
        :param steering:
        :return:
        """
        self.tank.drive(speed * 10, steering)

    def distance_to_rotation(self, distance):
        """
        calculation to convert the distance from
        cm into rotations.

        :param distance:  The distance in cm
        :return: The rotations to be traveled for the given distance
        """
        rotation = distance / self.circumference
        return rotation

    def distance_to_angle(self, distance):
        """
        calculation to convert the distance from
        cm into rotations.

        :param distance:  The distance in cm
        :return: The rotations to be traveled for the given distance
        """
        rotation = self.distance_to_rotation(distance) * 360.0
        return rotation

    def angle_to_distance(self, angle):
        """

        :param angle:
        :return:
        """
        d = self.circumference / 360.0 * angle
        return d

    def stop(self, brake=None):
        """
        stops all motors on all different drive modes

        :param brake: None, brake, coast, hold
        :return:
        """
        if not brake or brake == "brake":
            self.left.stop(Stop.BRAKE)
            self.right.stop(Stop.BRAKE)
            self.tank.stop(Stop.BRAKE)
        elif brake == "coast":
            self.left.stop(Stop.COAST)
            self.right.stop(Stop.COAST)
            self.tank.stop(Stop.COAST)
        elif brake == "hold":
            self.left.stop(Stop.HOLD)
            self.right.stop(Stop.HOLD)
            self.tank.stop(Stop.HOLD)

        self.still()

    def still(self):
        """

        :return:
        """

        PRINT("Still Start")

        count = 10
        angle_left_old = self.left.angle()
        angle_right_old = self.right.angle()
        while count > 0:
            angle_left_current = self.left.angle()
            angle_right_current = self.right.angle()
            if angle_left_current == angle_left_old and angle_right_current == angle_right_old:
                count = count - 1
            else:
                angle_left_old = angle_left_current
                angle_right_old = angle_right_current

        PRINT("Still Stop")

    def forward(self, speed, distance, brake=None):
        """

        :param speed:
        :param distance:
        :param brake:
        :return:
        """

        PRINT("Forward", speed, distance, brake)

        if distance < 0:
            speed = -speed
            distance = -distance

        self.reset()
        angle = abs(self.distance_to_angle(10 * distance))
        self.on(speed)

        run = True
        while run:
            current = abs(self.left.angle())
            run = current < angle

        self.stop(brake=brake)

        PRINT("Forward Stop")

    def on_forever(self, speed_left, speed_right):

        PRINT("on_forever", speed_left, speed_right)
        self.reset()

        self.left.run(speed_left * 10)
        self.right.run(speed_right * 10)

    def turn(self, speed, angle):
        """
        takes the radius of the robot and dives on it for a distance based on the angle
        :param speed:
        :param angle:
        :return:
        """

        PRINT("Turn", speed, angle)

        self.reset()

        c = self.axle_track * math.pi
        fraction = 360.0 / angle
        d = c / fraction
        a = self.distance_to_angle(d)

        self.left.run_angle(speed * 10, -a, Stop.BRAKE, False)
        self.right.run_angle(speed * 10, a, Stop.BRAKE, False)

        count = 10
        old = abs(self.left.angle())
        while abs(self.left.angle()) < abs(a) or abs(self.right.angle()) < abs(a):

            PRINT("TURN CHECK", count, old, abs(self.left.angle()), abs(self.right.angle()))
            if old == abs(self.left.angle()):
                count = count - 1
            else:
                old = abs(self.left.angle())

            if count < 0:
                PRINT("FORCED STOP IN TURN")
                self.beep()
                break
        self.stop()

        PRINT("Turn Stop")

    def turntoblack(self,
                    speed,
                    direction="left",
                    port=3,
                    black=10):
        """
        turns the robot to the black line.

        :param speed:
        :param direction:
        :param port:
        :param black:
        :return:
        """
        PRINT("turntoblack", speed, direction, port, black)

        if direction == "left":
            self.left.run(speed * 10)
        else:
            self.right.run(speed * 10)

        while self.light(port) > black:
            pass
        self.stop()

    def turntowhite(self,
                    speed,
                    direction="left",
                    port=3,
                    white=80):
        """
        turns the robot to the white line.

        :param speed:
        :param direction:
        :param port:
        :param white:
        :return:
        """
        PRINT("turntoblack", speed, direction, port, white)

        if direction == "left":
            self.left.run(speed * 10)
        else:
            self.right.run(speed * 10)

        while self.light(port) < white:
            pass
        self.stop()

    def aligntoblack(self, speed, port_left, port_right, black=10):
        """

        :param speed:
        :param port_left:
        :param port_right:
        :param black:
        :return:
        """

        PRINT("aligntoblack", speed, port, black)

        self.on_forever(speed, speed)
        left_finished = False
        right_finished = False

        while not left_finished and not right_finished:
            if self.light(port_left) < black:
                self.left.stop(Stop.BRAKE)
                left_finished = True
            if self.right(port_right) < black:
                self.right.stop(Stop.BRAKE)
                right_finished = True
        self.stop()

        PRINT("aligntoblack Stop")

    def aligntowhite(self, speed, port_left, port_right, white=80):
        """

        :param speed:
        :param port_left:
        :param port_right:
        :param white:
        :return:
        """

        PRINT("aligntoblack", speed, port, black)

        self.on_forever(speed, speed)
        left_finished = False
        right_finished = False

        while not left_finished and not right_finished:
            if self.light(port_left) > white:
                self.left.stop(Stop.BRAKE)
                left_finished = True
            if self.right(port_right) > white:
                self.right.stop(Stop.BRAKE)
                right_finished = True
        self.stop()

        PRINT("aligntowhite Stop")

    def gotoblack(self, speed, port, black=10):
        """
        The robot moves to the black line while using the sensor on the given port

        :param speed: The speed
        :param port: The port 1,2,3,4
        :param black: The value to stop
        """

        PRINT("aligntoblack", speed, port, black)

        self.left.run_angle(speed * 10, -a, Stop.BRAKE, False)
        self.right.run_angle(speed * 10, a, Stop.BRAKE, False)

        self.on(speed, 0)
        while self.light(port) > black:
            pass
        self.stop()

        PRINT("gotoblack Stop")

    def gotowhite(self, speed, port, white=90):
        """
        The robot moves to the white line while using the sensor on the given port

        :param speed: The speed
        :param port: The port 1,2,3,4
        :param white: The value to stop
        """

        PRINT("gotoblack", speed, port, white)

        self.on(speed, 0)
        while self.light(port) < white:
            pass
        self.stop()

        PRINT("gotowhite Stop")

    def followline(self,
                   speed=25,  # speed 0 - 100
                   distance=None,  # distance in cm
                   t=None,
                   port=3,  # the port number we use to follow the line
                   right=True,  # the side on which to follow the line
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
            value = self.light(port)  # get the light value

            # correction = delta + (factor * value)  # calculate the correction for steering
            correction = f * factor * (value + delta)
            # correction = f * correction  # if we drive backwards negate the correction

            self.on(speed, correction)  # switch the steering on with the given correction and speed

            # if the time is used we set run to false once the end time is reached
            # if the distance is greater than the position than the leave the
            angle = self.left.angle()

            traveled = self.angle_to_distance(angle)

            current = time.time()  # measure the current time
            if t is not None and current > end_time:
                break  # leave the loopK
            if distance is not None and distance < traveled:
                break  # leave the loop

        self.stop()  # stop the robot

    def calibrate(self, speed, distance=15, ports=[2, 3, 4], direction='front'):
        """

        :param speed:
        :param distance:
        :param ports:
        :param direction:
        :return:
        """

        self.reset()
        self.on(speed, 0)
        distance = self.distance_to_angle(distance * 10)

        while self.left.angle() < distance:

            for i in ports:
                self.colorsensor[i].set_white()
                self.colorsensor[i].set_black()
                PRINT(i,
                      self.colorsensor[i].black,
                      self.colorsensor[i].white)

        self.stop()

        for i in ports:
            PRINT(i, self.colorsensor[i].black, self.colorsensor[i].white)
