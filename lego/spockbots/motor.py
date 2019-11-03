from pybricks.robotics import DriveBase
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.parameters import Stop, Direction
import math


#######################################################
# Motor
#######################################################


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
