import math
import time

from pybricks import ev3brick as brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Button
from pybricks.parameters import Stop, Direction
from pybricks.robotics import DriveBase
# from pybricks.ev3devices import ColorSensor
# from spockbots.colorsensor import SpockbotsColorSensor
from spockbots.colorsensor import SpockbotsColorSensors
from spockbots.output import PRINT, voltage
from threading import Thread
import sys
from spockbots.output import led

#######################################################
# Motor
#######################################################


class SpockbotsMotor(object):


    def __init__(self, direction=None):
        """
        defines the large motors (left and right),
        the tank move, and the medium motors.

        :param direction: if the direction is 'forward'
                          the robot moves forward, otherwise
                          backwards.

        """
        self.running = True
        led("GREEN")
        self.diameter = round(62.4, 3)  # mm
        self.width = 20.0  # mm
        self.circumference = round(self.diameter * math.pi, 3)
        self.axle_track = 140.0 # not used, width between middle of tires
        self.direction = "forward"

        self.left, self.right, self.tank = \
            self.setup(direction=direction)

        self.colorsensors = SpockbotsColorSensors(ports=[2, 3, 4])



    def check_kill_button(self):
        """
        This will stop all motors  and finish the program.
        It can be used in the programs to check if the program should be
        finished early du to an error in the runs.
        """
        if Button.LEFT_UP in brick.buttons(): # backspace
            self.running = False
            led("RED")
            print("KILL")
            self.beep()
            self.beep()
            self.beep()
            self.beep()

            self.stop()
            self.left_medium.stop(Stop.BRAKE)
            self.right_medium.stop(Stop.BRAKE)
        return not self.running

    def sleep(self,seconds):

        if self.check_kill_button():
            return

        time.sleep(seconds)

    def beep(self):
        """
        robot will beep.

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
        return ""

    def setup(self, direction=None):
        """
        setup the direction, the motors, and the tank with the appropriate direction.

        :param direction: if the direction is 'forward' the robot moves forward, otherwise backwards.
        :return: left, right motors  and tank

        """
        if self.check_kill_button():
            return

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

        self.tank = DriveBase(self.left, self.right,
                              self.diameter, self.axle_track)

        self.left_medium = Motor(Port.D, Direction.CLOCKWISE)
        self.right_medium = Motor(Port.C, Direction.CLOCKWISE)

        return self.left, self.right, self.tank

    def value(self, port):
        """
        return the reflective color sensor value.

        :param port: the port number of the color sensor
        :return: the reflective color value

        """
        return self.colorsensors.value(port)

    def color(self, port):
        """
        return the reflective color sensor value.

        :param port: the port number of the color sensor
        :return: the reflective color value

        """
        return self.colorsensors.color(port)

    def reset(self):
        """
        resets the angle in the large motors to 0.

        """

        self.left.reset_angle(0)
        self.right.reset_angle(0)

    def on(self, speed, steering=0):
        """
        turns the large motors on while using steering.

        :param speed: the speed of the robot
        :param steering: an angle for the steering

        """

        self.tank.drive(speed * 10, steering)

    def distance_to_rotation(self, distance):
        """
        calculation to convert the distance from cm into rotations.

        :param distance:  The distance in cm
        :return: The rotations to be traveled for the given distance

        """

        rotation = distance / self.circumference
        return rotation

    def distance_to_angle(self, distance):
        """
        calculation to convert the distance from cm into angle.

        :param distance:  The distance in cm
        :return: The degrees traveled for the given distance

        """

        rotation = self.distance_to_rotation(distance) * 360.0
        return rotation

    def angle_to_distance(self, angle):
        """
        calculation to return the distance in cm given an angle.

        :param angle: the angle
        :return: distance in cm for turning an angle

        """

        d = self.circumference / 360.0 * angle
        return d

    def stop(self, brake=None):
        """
        stops all motors on all different drive modes.

        :param brake: None, brake, coast, hold

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

    def still(self, count=5):
        """
        waits till the motors are no longer turning.
        """

        PRINT("Still Start")

        angle_left_old = self.left.angle()
        angle_right_old = self.right.angle()
        while count > 0:
            angle_left_current = self.left.angle()
            angle_right_current = self.right.angle()
            if angle_left_current == angle_left_old and \
                    angle_right_current == angle_right_old:
                count = count - 1
            else:
                angle_left_old = angle_left_current
                angle_right_old = angle_right_current

        PRINT("Still Stop")

    def forward(self, speed, distance, brake=None):
        """
        the robot drives forward for a given distance.

        :param speed: speed of robot
        :param distance: distance that robot goes forward (in cm)
        :param brake: one of the values brake, hold, coast

        """
        if self.check_kill_button():
            return

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
        """
        turns motors on with left and right speed.

        :param speed_left: speed of left motor
        :param speed_right: speed of the right motor

        """
        if self.check_kill_button():
            return

        PRINT("on_forever", speed_left, speed_right)
        self.reset()

        self.left.run(speed_left * 10)
        self.right.run(speed_right * 10)

    def turn(self, speed, angle, count=5):
        """
        takes the radius of the robot and dives on it
        for a distance based on the angle.

        :param speed: speed of turn
        :param angle: angle of turn

        """
        if self.check_kill_button():
            return

        PRINT("Turn", speed, angle)

        self.reset()

        c = self.axle_track * math.pi
        fraction = 360.0 / angle
        d = c / fraction
        a = self.distance_to_angle(d)

        self.left.run_angle(speed * 10, -a, Stop.BRAKE, False)
        self.right.run_angle(speed * 10, a, Stop.BRAKE, False)

        old = abs(self.left.angle())
        while abs(self.left.angle()) < abs(a) or \
                abs(self.right.angle()) < abs(a):

            PRINT("TURN CHECK", count, old,
                  abs(self.left.angle()),
                  abs(self.right.angle()))
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

    def turntocolor(self,
                    speed,
                    direction="left",
                    port=2,
                    colors=[6]):
        """
        turns the robot to the black line.

        :param speed: speed of turn
        :param direction: left or right
        :param port: port of color sensor
        :param black: value of black

        """
        if self.check_kill_button():
            return

        PRINT("turntocolors", speed, direction, port, colors)

        if direction == "left":
            self.left.run(speed * 10)
        else:
            self.right.run(speed * 10)

        while self.color(port) not in colors:
            pass
        self.stop()

    def turntoblack(self,
                    speed,
                    direction="left",
                    port=3,
                    black=10):
        """
        turns the robot to the black line.

        :param speed: speed of turn
        :param direction: left or right
        :param port: port of color sensor
        :param black: value of black

        """
        if self.check_kill_button():
            return

        PRINT("turntoblack", speed, direction, port, black)

        if direction == "left":
            self.left.run(speed * 10)
        else:
            self.right.run(speed * 10)

        while self.value(port) > black:
            pass
        self.stop()

    def turntowhite(self,
                    speed,
                    direction="left",
                    port=3,
                    white=80):
        """
        turns the robot to the white line.

        :param speed: speed of turn
        :param direction: left or right
        :param port: port of color sensor
        :param white: value of white

        """
        if self.check_kill_button():
            return

        PRINT("turntowhite", speed, direction, port, white)

        if direction == "left":
            self.left.run(speed * 10)
        else:
            self.right.run(speed * 10)

        while self.value(port) < white:
            pass
        self.stop()

    def aligntoblack(self, speed, port_left, port_right, black=10):
        """
        aligns with black line while driving each motor.

        :param speed: speed of robot
        :param port_left: port of left color sensor
        :param port_right: port of right color sensor
        :param black: value of black

        """
        if self.check_kill_button():
            return

        PRINT("aligntoblack", speed, port_left, port_right, black)

        self.on_forever(speed, speed)
        left_finished = False
        right_finished = False

        while not (left_finished and right_finished):
            left_light = self.value(port_left)
            right_light = self.value(port_right)
            PRINT("Light", left_light, right_light)
            if left_light < black:
                self.right.stop(Stop.BRAKE)
                left_finished = True
            if right_light < black:
                self.left.stop(Stop.BRAKE)
                right_finished = True
        self.stop()

        PRINT("aligntoblack Stop")

    def aligntowhite(self, speed, port_left, port_right, white=80):
        """
        aligns with white line while driving each motor.

        :param speed: speed of robot
        :param port_left: port of left color sensor
        :param port_right: port of right color sensor
        :param white: value of white

        """
        if self.check_kill_button():
            return

        PRINT("aligntoblack", speed, port_left, port_right, white)

        self.on_forever(speed, speed)
        left_finished = False
        right_finished = False

        while not (left_finished and right_finished):
            left_light = self.value(port_left)
            right_light = self.value(port_right)
            PRINT("Light", left_light, right_light)
            if left_light > white:
                self.right.stop(Stop.BRAKE)
                left_finished = True
            if right_light > white:
                self.left.stop(Stop.BRAKE)
                right_finished = True
        self.stop()

        PRINT("aligntowhite Stop")

    def alignonblackline(self, speed, port_left, port_right, black, white):
        #s
        self.aligntoblack(speed, port_left, port_right, black)
        self.aligntoblack(-speed, port_left, port_right, black)
        self.aligntowhite(speed/2, port_left, port_right, white)
        self.aligntoblack(-speed/2, port_left, port_right, black)




    def gotoblack(self, speed, port, black=10):
        """
        robot moves to the black line while using the
        sensor on the given port.

        :param speed: speed of robot
        :param port: port of color sensor
        :param black: value of black

        """
        if self.check_kill_button():
            return

        PRINT("gotoblack", speed, port, black)

        # self.left.run_angle(speed * 10, -a, Stop.BRAKE, False)
        # self.right.run_angle(speed * 10, a, Stop.BRAKE, False)

        self.on(speed, 0)
        while self.value(port) > black:
            pass
        self.stop()

        PRINT("gotoblack Stop")

    def gotowhite(self, speed, port, white=90):
        """
        robot moves to the white line while using
        the sensor on the given port.

        :param speed: speed of robot
        :param port: port of color sensor
        :param white: value of white

        """
        if self.check_kill_button():
            return

        PRINT("gotowhite", speed, port, white)

        self.on(speed, 0)
        while self.value(port) < white:
            pass
        self.stop()

        PRINT("gotowhite Stop")

    def gotocolor(self, speed, port, colors=[0]):
        """
        robot moves to the black line while using the
        sensor on the given port.

        :param speed: speed of robot
        :param port: port of color sensor
        :param black: value of black

        """
        if self.check_kill_button():
            return

        PRINT("gotocolor", speed, port, colors)

        self.on(speed, 0)
        run = True
        while run:
            value = self.color(port)
            print("COLOR", value)
            run = value not in colors
        self.stop()

        PRINT("gotocolor Stop")

    def followline(self,
                   speed=25,  # speed 0 - 100
                   distance=None,  # distance in cm
                   t=None,
                   port=3,  # the port number we use to follow the line
                   right=True,  # the side on which to follow the line
                   stop_color_sensor=None,
                   stop_values=None,  # [4,5]
                   stop_color_mode=None,  # color, reflective
                   delta=-35,  # control smoothness
                   factor=0.4):  # parameters to control smoothness

        """
        follows line for either a distance or for time.

        :param speed: speed of robot
        :param distance: distance that robot follows line
        :param t: time that robot follows line for
        :param port: port of color sensor
        :param right: whether the robot is following
                      the right or left side of line
        :param black: black value
        :param white: white value
        :param delta: adjustment value to convert from color
                      sensor values (0 to 100) to motor
                      steering (-100 to 100)
        :param factor: factor of adjustment, controls smoothness

        """
        if self.check_kill_button():
            return

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
            if self.check_kill_button():
                return

            value = self.value(port)  # get the light value

            # correction = delta + (factor * value)
            # calculate the correction for steering
            correction = f * factor * (value + delta)
            # correction = f * correction
            # if we drive backwards negate the correction

            self.on(speed, correction)
            # switch the steering on with the given correction and speed

            # if the time is used we set run to
            #        false once the end time is reached
            # if the distance is greater than the
            #        position than the leave the
            angle = self.left.angle()

            traveled = self.angle_to_distance(angle)

            current = time.time()  # measure the current time
            if t is not None and current > end_time:
                break  # leave the loopK
            if distance is not None and distance < traveled:
                break  # leave the loop
            if stop_color_sensor is not None:
                if stop_color_mode == "color":
                    value = self.color(port)
                elif stop_color_mode == "reflective":
                    value = self.value(port)
                print("VALUE", value)
                if value in stop_values:
                    break  # leave the loop

        self.stop()  # stop the robot

    def calibrate(self, speed, distance=15, ports=[2, 3, 4], direction='front'):
        """
        calibrates color sensors by driving over black and white line.

        :param speed: speed of robot
        :param distance: distance that robot travels
        :param ports: ports of color sensors
        :param direction: direction of calibration

        """
        if self.check_kill_button():
            return

        self.reset()
        self.on(speed, 0)
        distance = self.distance_to_angle(distance * 10)

        while self.left.angle() < distance:

            for i in ports:
                self.colorsensors.colorsensor[i].set_white()
                self.colorsensors.colorsensor[i].set_black()
                PRINT(i,
                      self.colorsensors.colorsensor[i].black,
                      self.colorsensors.colorsensor[i].white)

        self.stop()

        for i in ports:
            PRINT(i,
                  self.colorsensors.colorsensor[i].black,
                  self.colorsensors.colorsensor[i].white)

    # followline_pid(distance=45, port=3, speed=20, black=0, white=100, kp=0.3, ki=0.01, kd=0.0)
    def followline_pid(self,
                       debug=False,
                       distance=None,  # distance in cm
                       t=None,
                       right=True,  # the side on which to follow the line
                       stop_color_sensor=None,
                       stop_values=None,  # [4,5]
                       stop_color_mode=None,  # color, reflective
                       port=3, speed=25, black=0, white=100, kp=0.3, ki=0.0, kd=0.0):
        if self.check_kill_button():
            return

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

        integral = 0

        midpoint = (white - black) / 2 + black
        lasterror = 0.0

        loop_start_time = current = time.time()

        print("kp=", kp, "ki=", ki, "kd=", kd)
        while True:
            if self.check_kill_button():
                return
            try:
                value = self.value(port)  # get the light value

                error = midpoint - value
                integral = error + integral
                derivative = error - lasterror

                correction = f * kp * error + ki * integral + kd * derivative

                lasterror = error

                self.on(speed, correction)
                # switch the steering on with the given correction and speed

                # if the time is used we set run to
                #        false once the end time is reached
                # if the distance is greater than the
                #        position than the leave the
                angle = self.left.angle()
                traveled = self.angle_to_distance(angle)
                current = time.time()  # measure the current time

                if debug:
                    if correction > 0.0:
                        bar = str(30 * ' ') + str('#' * int(correction))
                    elif correction < 0.0:
                        bar = ' ' * int(30 + correction) + '#' * int(abs(correction))
                    else:
                        bar = 60 * ' '

                    print("{:4.2f} {:4.2f} {:4.2f} {:3d} {}".format(correction, traveled, current - loop_start_time,
                                                                    value, bar))

                if t is not None and current > end_time:
                    break  # leave the loopK
                if distance is not None and distance < traveled:
                    break  # leave the loop
                if stop_color_sensor is not None:
                    if stop_color_mode == "color":
                        value = self.color(port)
                    elif stop_color_mode == "reflective":
                        value = self.value(port)
                    print("VALUE", value)
                    if value in stop_values:
                        break  # leave the loop
            except Exception as e:
                print(e)
                break
        self.stop()  # stop the robot
