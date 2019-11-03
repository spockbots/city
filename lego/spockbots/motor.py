from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.parameters import Stop, Direction
import math
from pybricks.ev3devices import ColorSensor
import time

#######################################################
# Motor
#######################################################

colorsensor = [None,None,None,None,None]

class SpockbotsColorSensor(object):

    def __init__(self, port=3):
        if port == 1:
            self.sensor = ColorSensor(Port.S1)
        elif port == 2:
            self.sensor = ColorSensor(Port.S2)
        elif port == 3:
            self.sensor = ColorSensor(Port.S3)
        elif port == 4:
            self.sensor = ColorSensor(Port.S4)

    def light(self):
        return self.sensor.reflection()


for i in [2,3,4]:
    colorsensor[i] = SpockbotsColorSensor(port=i)

class SpockbotsMotor(object):

    def __init__(self, direction=None):

        self.diameter = round(62.4, 3)  # mm
        self.width = 20.0  # mm
        self.circumference = round(self.diameter * math.pi, 3)  # as diameter is in mm
        self.axle_track = round(8.0 * 14, 3)


        self.left, self.right, self.tank = self.setup(direction=direction)

    def __str__(self):
        print()
        print("Robot Info")
        print("============================----------")
        print("Tire Diameter:", self.diameter)
        print("Circumference:", self.circumference)
        print("Tire Width:   ", self.width)
        print("Axle Track:   ", self.axle_track)
        print("Angle Left:   ", self.left.angle())
        print("Angle Right:  ", self.right.angle())
        print("Direction:    ", self.direction)

        print()

    def setup(self, direction=None):

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

        return self.left, self.right, self.tank

    def light(self, port):
        return colorsensor[port].light()

    def reset(self):
        self.left.reset_angle(0)
        self.right.reset_angle(0)

    def on(self, speed, steering=0):
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
        d = self.circumference / 360.0 * angle
        return d

    def stop(self, brake=None):
        """
        stops all motors on all different drive modes

        :param brake: None, brake, coast, hold
        :return:
        """
        """
    
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

    def forward(self, speed, distance, brake=None):

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


    def turn(self, speed, angle):
        """
        takes the radius of the robot and dives on it for a distance based on the ancle
        :param speed:
        :param angle:
        :return:
        """
        self.reset()

        c = self.axle_track * math.pi
        fraction = 360.0 / angle
        d = c / fraction
        a = self.distance_to_angle(d)

        self.left.run_angle(speed * 10, -a, Stop.BRAKE, False)
        self.right.run_angle(speed * 10, a, Stop.BRAKE, False)

        while abs(self.left.angle()) < abs(a) or abs(self.right.angle()) < abs(a):
            pass
        self.stop()


    def gotoblack(self, speed, port, black=10):
        """
        The robot moves to the black line while using the sensor on the given port

        :param speed: The speed
        :param port: The port 1,2,3,4
        :param black: The value to stop
        """
        self.on(speed, 0)
        while self.light(port)  > black:
            pass
        self.stop()


    def gotowhite(self, speed, port, white=90):
        """
        The robot moves to the white line while using the sensor on the given port

        :param speed: The speed
        :param port: The port 1,2,3,4
        :param white: The value to stop
        """

        self.on(speed, 0)
        while self.light(port) < white:
            pass
        self.stop()


    def followline(self,
            speed=25,    # speed 0 - 100
            distance=None, # distance in cm
            t=None,
            port=3,      # the port number we use to follow the line
            right=True,  # the side on which to follow the line
            black=0,     # minimal balck
            white=100,   # maximal white
            delta=-35,   # paramaters to control smoothness
            factor=0.7): # parameters to control smoothness

        if right:
            f = - 1.0
        else:
            f = 1.0

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

            current = time.time()  # measure the crurrent time
            if t is not None and current > end_time:
                break  # leave the loopK
            if distance is not None and distance < traveled:
                break  # leave the loop

        self.stop()  # stop the robot

