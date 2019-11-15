Lessons
=======

.. note:: PLEASE NOTE THAT ALL LIBRARY CLASSES METHODS AND FUNCTIONS HAVE PREVIOUSLY BEEN
          DEVELOPED OVER A PERIOD OF 2 YEARS BY THE

            SPOCKBOTS TEAM

          USING THE MINDSORM GUI. THIS DOCUMENT HAS BEEN CREATED TO DEMONSTRATE HOW THIS
          LIBRARY WAS CONVERTED.

.. note:: However, some ideas were discussed and explicitly targeted as lessons, such as
          how to design a more reliable Gyro reset, and how to deal with the different black/white
          values when using more than one color sensor.

          We found that through structured activities such enhancements are possible
          to be developed by the team. Guidance from the coach was integrated in the solutions.
          Just as a teacher points out wrong problems to solutions it is important for the coach to
          provide suggestions for debugging the code. Which we have done. However, as explained in
          the pitfalls of python some aspects are currently beyond the needed scope for the teams using
          Python and we encourace LEGO to improve their library with feedback from those having used
          Python on the EV3 extensively

.. warning:: Although python could be used by beginning teams, we find that due to some current
             limitations beginning teams should use the GUI and not python.

Python Programming Templates and Activities
-------------------------------------------

The activities conducted by the team were centered around a number of
coordinated educational interactions with a subset of team members.
Due to extensive travel and time constraints of some team members and
focus on other portions they could not participate in these
activities.

As a coach I put together this material so that they or even other
teams can benefit form this information. For example I am planning to
visit the regional Elementary School to
discuss expansion and potential adoption of the material into local
schools. The reason we target elementary schools is that we believe
this material can be taught on that grade level with the help of a
qualified teacher.

Color Sensor
------------

Goals:

* Learn about classes
* Learn how to read and write files
* Learn how to use try/except
* Learn how to pass paramaters to an method on initialization
* Leran how to use vriables start with `self.` in other methods
* Learn how to map values between 0 and 100

Problem: In our first exercise we are exploring the color
sensor. Often you only have a single color sensor, but when looking at
the different sensors in your kits, they may all behave slightly
differently. What registers as black 8 on one sensor may register as
black 15 on another. The same is valid with white, we may see values
such as 80, 100, and so on.

However we know that the color values are always between 0 - 100.
With one significant issue. Once in a while no value is returned and
if we were to expect an integer we need to make sure that Python can
react towards such errors.

As we also want you to learn about classes in Python we provide you
with a template that you need to complete. Please revisit our Python
material and look at how we define classes. Now let us define a class
for a `better` Color sensor and we call this class

    `SpockbotsColorSensor`

We do the usual things such as importing the needed abstractions from the
pybricks and python libraries. We have provided this as an example for you.

We also demonstrate how to initialize the color sensor while
you can pass along simply the port number so you can reflect once more
on which conditions work. The keyword `self` can be most simply
understood while knowing that programmers do not like to always write
the class name, so they use self in this particular case.

The init class also contains a number of variables that we can access
within other methods defined as part of this class. We also showcase yohow
to define simple methods while leveraging other variables such as the `self.sensor`
we define in the init method.
In the class methods `reflection()` and `color()`. What would happen if the
color sensor cuts out or does not read a value. To avoid this case we simply
put a loop around the method that returns the value. We simply try if it
works and if it does, then return a value if not it tries it again.

We store the minimum black and maximum white values that we are
detected under the current light conditions.

You have the following tasks:

#. Understand the set_white function and implement an equivalent black function
#. Implement a function value() that always returns the mapped color values
#. In case we have more than one color sensor its sometimes interesting to
   see which one is which, thus this function just flashes the sensor by
   switching to different modes
#. As we have not yet talked about files, we would like to take this example to
   teach you about how to write files in Python. This is demonstrated in
   the write function and it shows how to write values to a file. We also
   provide you with a read function so you know how to read a file.  The
   read function also shows how easy it is to use try and except. In case
   the file would not be there, and we call read we get an error. When
   reading the values we must make sure that the order is the same when
   we write it.


Now after you have written the better sensor class let us see how we use it

The sensor is stored in a directory called `spockbots` that has a file __init__.py in it
this allows us to import the sensor class into a program as follows, while
reading a value and wait for a while until we read the next value and print it out.

Experiment and move the sensor over various different places to measure the difference.


::

    from spockbots.colorsensor import SpockbotsColorSensor
    from time import sleep

    colorsensor = SpockbotsColorSensor(2) # we assume you put the sensor on port 2

    colorsensor.black = 8    # finding the minimum black value you need to do, use port view
    colorsensor.white = 90   # finidng the maximum white value you need to do, use port view

    while True:
        value = colorsensor.value()
        print(value)
        sleep(0.5)


Next, modify the program to print th color instead of the reflective value.


Here is the template for this assignment to complete the file `colorsensor.py`:

::

    from time import sleep
    from pybricks import ev3brick as brick
    from pybricks.ev3devices import ColorSensor
    from pybricks.parameters import Port


    class SpockbotsColorSensor:
        """
        defines a Colorsensor with values between 0 and 100
        """

        def __init__(self, port=3):
            """

            :param port: the port
            :param speed: teh speed for calibration
            """
            """
            :param: number  number of color sensor on ev3
            """
            if port == 1:
                self.sensor = ColorSensor(Port.S1)
            elif port == 2:
                self.sensor = ColorSensor(Port.S2)
            elif port == 3:
                self.sensor = ColorSensor(Port.S3)
            elif port == 4:
                self.sensor = ColorSensor(Port.S4)

            self.port = port
            self.black = 100
            self.white = 0


        def reflection(self):
            """
            gets the reflection from the sensor

            :return: the original reflective lit value without
            """
            while True:
                try:
                    return self.sensor.reflection()
                except:
                    pass

        def color(self):
            """
            returns the color value

            :return: the color value
            """
            #
            # how would you write a function for returning always a color value
            # even if the sensor cuts out. see the reflection() method for an example.
            #

        def set_white(self):
            """
            sets the current value to white if its higher than what is stored
            :return:
            """
            value = self.sensor.reflection()
            if value > self.white:
                self.white = value

        def set_black(self):
            """
            sets the current value to black if it is smaller than what is stored
            """
            #
            # PLEASE PUT YOUR CODE HERE
            #

        def value(self):
            """
            reads the current value mapped between 0 and 100.
            :return: returns the reflective light mapped between 0 to 100
            """

            # read the current color value
            # map the value between 0 to 100 while using the minimum black and maximum white value
            # Make sure to only return values between 0 and 100 while testing it
            #
            # use the variable v and return it at the end. Remember functions can return values

            return v

        def flash(self):
            """
            flashes the color sensor by switching between
            color and reflective mode
            """
            #
            # make the sensor flash
            #

        def write(self):
            """
            append the black and white value to a file
            """
            f = open("/home/robot/calibrate.txt", "w+")
            f.write(str(self.sensor.black) + "\n")
            f.write(str(self.sensor.white) + "\n")
            f.close()

        def read(self):
            """
            reads the color sensor data form the file
            :return:
            """
            try:
                f = open("/home/robot/calibrate.txt", "r")
                self.colorsensor[port].black = int(f.readline())
                self.colorsensor[port].white = int(f.readline())
                f.close()
            except:
                print("we can not find the calibration file")

        def info(self):
            """
            prints the black and white value read form the
            sensor
            """
            #
            # write a print statement that prints out the information for this color sensor such as
            # port, black, and white
            #

Three color sensors
-------------------

Now we have a beautiful example for a Python class in our color sensor. The next lesson will
introduce you to how you can use the same class to define a new one that includes a number of colorsensors.
We specify the ports simply as a list at time of creation. So our goal is to do something like


::

    colorsensors = SpockbotsColorSensors(port=[2,3,4])
    # drive over the black line
    # and find the black white values for all sensors
    colorsensor.calibrate(port=[2,3,4])
    colorsensors.write(port=[2,3,4])


Now we can use it in a program as follows to print repeatedly the
values from all sensors every half second

::

    colorsensors = SpockbotsColorSensors(port=[2,3,4])
    colorsensors.read(port=[2,3,4])

    while True:
        print (colorsensors.value(2),
               colorsensors.value(3),
               colorsensors.value(4))
        time.sleep(0.5)

Here is the template for the multi color sensor class

::

    class SpockbotsColorSensors:
        """

        This is how we create the sensors:

            colorsensor = SpockbotsColorSensors(ports=[2,3,4])
            colorsensor.read()

        Now you can use

            colorsensor[i].value()

        to get the reflective value of the colorsensor on port i.
        To get the color value we can use

            colorsensor[i].color()

        """

        def __init__(self, ports=[2, 3, 4], speed=5):
            """
            Creates the color sensors for our robot.
            Once calibrated, the sensor values always return 0-100,
            where 0 is black and 100 is white

            :param ports: the list of ports we use on the robot for color sensors
            :param speed: The speed for the calibration run
            """
            self.ports = ports
            self.speed = speed
            self.colorsensor = [None, None, None, None, None]
                # in python lists start from 0 not 1
                # so we simply do not use the first element in the list
            # our robot uses only
            #  colorsensor[2]
            #  colorsensor[3]
            #  colorsensor[4]
            #  the ports are passed along as a list [2,3,4]
            self.ports = ports
            for i in ports:
                print("SETUP COLORSENSOR", i)
                self.colorsensor[i] = SpockbotsColorSensor(port=i)

        def value(self, i):
            """
            returns the reflective value between 0-100 after
            calibration on the port i

            :param i: number of the port
            :return: the reflective color value
            """
            # return the reflective value form the port i

        def color(self, i):
            """
            returns the color value between 0-100 after
            calibration on the port i

            :param i: number of the port
            :return: The color value, blue = 2
            """
            # return the color value from the port i

        def write(self, ports=[2, 3, 4]):
            """
            writes the black and white values to the file
            calibrate.txt

            :param ports: the ports used to write
            """
            # write the min black and maximum white to a file


        def read(self, ports=[2, 3, 4]):
            """
            reads the black and white values to the file
            calibrate.txt

            The values must be written previously. If the file
            does not exists a default is used.
                2: 0, 100
                3: 0, 100
                4: 4, 40    # because it is higher up so white does
                              not read that well
            """
            #
            # loop over the ports and read in the values from the file
            #

        def flash(self, ports=[2, 3, 4]):
            """
            Flashes the light sensor on teh ports one after another

            :param ports: the list of ports to flash
            """
            #
            # loop over the porst and flash the color sensor
            #



Driving The Robot
-----------------

Now it's time to drive around with our robot and our improved color sensors. So what we have to do is
simple create a class that includes all the Robot motors and Sensors.  So lets get started.
First, you must import all the needed classes from pybrics and Python. This includes a long list and
you can find them in our template

We simply call the class `SpockbotsMotor`. We define in that calss basic parameters such as wheel size
Naturally, we need a left and right motor, but also want to access the motor as part of a tank to do
steering just the same way as we do it in the GUI version. In addition we need to create as many color
sensors as your robot has, in case of the Spockbots team they decided to use three.

One function that is not provided by Python is a kill button when something goes wrong. To achieve this
we simply create a kill method, that sets a variable called `self.running` to false. This function returns
True if the LEFT_UP button is pressed.

we can then use it in functions in an if condition such as

::

    def forward(speed, direction):

        if check_kill_button(self):
            return

And if the button is pressed the program running variable is set. Within the function we first check if running is
False, we know the button has previously been pressed and thus the check button will be True. The return in the
function simply means that you leave the function once it reaches the return.
We know this function is not ideal but is good enough for us to try things out and if things do not go well we can at
least try to stop the robot. To demonstrate its use we like you to take a look at the sleep function. naturally we do
not like to sleep if the button has been pressed. This is just how we use it elsewhere. We even can
use the check_kill_button in loops to leave the loops when the button is pressed.

The setup method includes all the motor variables so we have values such as self.left, self.right, and self.tank
That we can use in the robot.

Sometimes programmers like to make things simple. As writing `self.colorsensors.value(port)` to get the refelctive
value on the given port it seems more convenient to create a method that can abbreviate things such as
`self.value(port)`

So insead of writing

::

    robot = SpockbotsMotor(direction="backwards")
    light = self.colorsensors.value(2)
    light = self.colorsensors.color(2)

we can simply write

::
        light_value = self.value(2)
        color_value = self.color(2)

Next write a function on how to reset the angle in the left and right motors to 0.
This will be useful when we measure the distance traveled.


In our next tasks we will calculate which distance we traveled given an angle from the motor or the rotations.
We use the circumferance for this and apply the formula that you need to research.

There are various methods that the spockbots team developed in previous years to be found useful.
Reimplement these methods in Python.

::

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
    from spockbots.output import PRINT
    from threading import Thread
    import sys
    from spockbots.output import led

    #######################################################
    # Robot
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

            print()
            print("Robot Info")
            print("============================")
            print("Tire Diameter:", self.diameter)
            print("Circumference:", self.circumference)
            print("Tire Width:   ", self.width)
            print("Axle Track:   ", self.axle_track)
            print("Angle Left:   ", self.left.angle())
            print("Angle Right:  ", self.right.angle())
            print("Direction:    ", self.direction)




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
            resets the angle in the large motors left and right to 0.

            """
            #
            # write the function that resets the motor
            #

        def on(self, speed, steering=0):
            """
            turns the large motors on while using steering.

            :param speed: the speed of the robot
            :param steering: an angle for the steering

            """
            # switch on the motor, but use a speed between 0 t 100. as the ev3 function require
            # values from 0 to 1000 we simply multiply the speed by 10

        def distance_to_rotation(self, distance):
            """
            calculation to convert the distance from cm into rotations.

            :param distance:  The distance in cm
            :return: The rotations to be traveled for the given distance

            """

            #
            # what is the rotation traveled using a given circumferance in cm
            # return rotation

        def distance_to_angle(self, distance):
            """
            calculation to convert the distance from cm into angle.

            :param distance:  The distance in cm
            :return: The degrees traveled for the given distance

            """
            #convert a distance to the angle travelde.
            return distance

        def angle_to_distance(self, angle):
            """
            calculation to return the distance in cm given an angle.

            :param angle: the angle
            :return: distance in cm for turning an angle

            """
            convert  the angle to a distance
            return d

        def stop(self, brake=None):
            """
            stops all motors on all different drive modes.

            :param brake: None, brake, coast, hold

            """
            #
            # This function just stops all the large motors and waits until the robot no longer moves
            #
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
            waits until the motors are no longer turning.
            """
            # Implement a function that tells if the robot is still, you can use
            # the motor angle or the gyro sensor

            PRINT("Still Stop")

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
            #
            # write a function that turns while only spinning the right motor till it
            # finds any of the colors in the list
            #

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
            #
            # write a function that truns while only spinning the right motor till it finds a black line
            #

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
            #
            # write a function that turns while only spinning the right motor till it finds a white line
            #

        def aligntoblack(self, speed, port_left, port_right, black=10):
            """
            aligns with black line while driving each motor.

            :param speed: speed of robot
            :param port_left: port of left color sensor
            :param port_right: port of right color sensor
            :param black: value of black

            """
            #
            # write a method that drives up to a black line while using the front color sensors
            #

        def aligntowhite(self, speed, port_left, port_right, white=80):
            """
            aligns with white line while driving each motor.

            :param speed: speed of robot
            :param port_left: port of left color sensor
            :param port_right: port of right color sensor
            :param white: value of white

            """
           #
            # write a method that drives up to a black line while using the front color sensors
            #

        def alignonblackline(self, speed, port_left, port_right, black, white):
            # Sandra contribt=uted this code
            # as we drive up to a line, we slighty my drive over it.
            # This method drives bacb and forth to find a better allignment

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
            #
            # drive forward till the light sensor on the given port returns black
            #

        def gotowhite(self, speed, port, white=90):
            """
            robot moves to the white line while using
            the sensor on the given port.

            :param speed: speed of robot
            :param port: port of color sensor
            :param white: value of white

            """
            #
            # drive forward till the light sensor on the given port returns white
            #


        def gotocolor(self, speed, port, colors=[0]):
            """
            robot moves to the black line while using the
            sensor on the given port.

            :param speed: speed of robot
            :param port: port of color sensor
            :param black: value of black

            """
            #
            # drive forward till the light sensor on the given port returns a color for the given list
            #


        def calibrate(self, speed, distance=15, ports=[2, 3, 4], direction='front'):
            """
            calibrates color sensors by driving over black and white line.

            :param speed: speed of robot
            :param distance: distance that robot travels
            :param ports: ports of color sensors
            :param direction: direction of calibration

            """
            #
            # you have decided to have 3 color sensors, write a program that drives
            # over the black line to calibrate it for balck and white and write the
            # values to a file
            #




Gyro Sensor
-----------

Goal:

* Learn about passing functions as parameter (Advanced Python concept)
* Learn how to turn the Gyro more precisely while making corrections
* Learn how to drive forward while minimizing the "jump" when using high speeds in forward
* Learn how to write a simple Gyro straight function similar to a line following function
* Learn how to more reliably reset the Gyro
* Learn how to deal with values missing from the Gyro (same as color values)

Going forward with the robot and turning is an elementary task that
needs to be implemented. The robot has two different ways of accomplishing this.

First it can be achieved while probing the motors that store an angle
reporting back how much the motor has turned. However, what the
Spockbots team found is although the motor forward is convenient, it
often does not return the desired result, e.g. when the robot caries a
heavy unbalanced load it may turn to the one or other side.

Second, you can use the Gyro sensor that measures the angle and speed
the robot turns.  While the gyro sensor is not very precise, it allows adequate results.
When you experiment with the Gyro sensor you will notice the following issues

#. when turning it may turn too much as you turn with a speed and braking takes time
#. when starting the robot with highspeed to go forward the robot "jumps" and when
   dropping often looses its orientation.

So let us discuss how we deal with the issue while using a Gyro Server
template that you will gradually improve.

In Python we have these issues

#. Sensor value is not 0 after reset
#. Sensor value drifts after reset as it takes time to settle down
#. Sensor drifts forever and never settles
#. Sensor value is not returned as no value is available from the sensor

You are expected to write a code that fixes this

Tasks and lessons

#. Conceptualize that the robot can go forward and backwards, for this
   reason the Gyro can count clockwise or counter clockwise.
   The direction is the same as your robot's direction
#. Conceptualize the angle function and compare it with the Color sensor.
   The while loop with the try except deals with missing values.
#. (Optional) Please change the code so that instead of looping use the last
   previous valid angle.
#. Define a reset method that waits till the gyro is still and the angle is 0
#. Develop methods for turning left
#. Develop methods for turning right
#. Integrate the left and right method in a better turn method. This method checs at
   the end if its at the expected angle, and if not corrects it while moving at a
   slow speed.
#. Test out your robot to see how accurate the turn is
#. Define a move forward function that avoids the "jump" and making the gyro start problematic
   Remember sometimes if we move slow we are more precise. Can you accelerate your robot from slow to fast.
   Use a proportional line following algorithm. You developed that as part of your previous mindstorm GUI library


::

    import sys
    import time
    from time import sleep

    from pybricks.ev3devices import GyroSensor
    from pybricks.parameters import Direction
    from pybricks.parameters import Port
    from spockbots.output import led, PRINT, beep, sound, signal


    class SpockbotsGyro(object):

        def __init__(self, robot, port=1):
            """
            Initializes the Gyro Sensor

            :param robot: robot variable that includes robot.tank so we can use steering
            :param port: port number for gyro sensor 1,2,3,4
            :param direction: if front if we drive forward
                              otherwise backwards
            """

            self.robot = robot
            if robot.direction == "forward":
                sensor_direction = Direction.CLOCKWISE
            else:
                sensor_direction = Direction.COUNTERCLOCKWISE

            found = False
            while not found:
                print("FINDING GYRO")
                try:
                    if port == 1:

                        self.sensor = GyroSensor(Port.S1, sensor_direction)
                    elif port == 2:
                        self.sensor = GyroSensor(Port.S2, sensor_direction)
                    elif port == 3:
                        self.sensor = GyroSensor(Port.S3,  sensor_direction)
                    elif port == 4:
                        self.sensor = GyroSensor(Port.S4,  sensor_direction)

                    print("SENSOR:", self.sensor)

                except Exception as e: # the gyro is not attched, please plug it in and out
                    signal()
                    beep()
                    if "No such sensor on Port" in str(e):
                        print()
                        print("ERROR: The Gyro Sensor is disconnected")
                        print()
                        sys.exit()

            print("GYRO INITIALIZED")

        def angle(self):
            """
            Gets the angle

            :return: The angle in degrees
            """
            while True:
                try:
                        a = self.sensor.angle()
                        self.last_angle = a
                return a
                    except:
                        print("Gyro read error")
                pass

        def zero(self):
            """
            set the gyro angle to 0
            :return:
            """
            self.sensor.reset_angle(0)

        def still(self, count=10):
            """
            tests if robot does not move for maximum count times and returns when it reaches 0
            :return: True if robot does not move
            """
            #
            # write a code that tests if the speed of the sensor is 0
            #

        def reset(self, count=10):
            """
            safely resets the gyro
            """
            #
            # resets the gyro and
            # waits till it is still
            # if it is not still it repeats this maximum count times

        def turn(self, speed=25, degrees=90, offset=None):
            """
            uses gyro to turn positive to right negative to left. As it may turn too much, it
            will correct itself at a lower speed and turn. As the sensor is accurate to 2
            degrees, we only do the correction if the robot is more than two degrees off.

            :param speed: speed it turns at
            :param degrees: degrees it turns
            :return:
            """
        #
        # Implement this function
        #
        # use the left and right function to make it easier for you

        def left(self, speed=25, degrees=90, offset=0):
            """
            The robot turns left with the given number of degrees

            :param speed: The speed
            :param degrees: The degrees
            :param offset:
            :return:
            """
            #
        # Implement this method
        #

        # remember the function to run is self.robot.on_forever(speed, -speed)

        def right(self, speed=25, degrees=90, offset=0):
            """
            The robot turns right with the given number of degrees

            :param speed: The speed
            :param degrees: The degrees
            :param offset:
            :return:
            """
        # Implement this method
        # compare it to what you implemented in left


        def forward(self,
                    speed=10,  # speed 0 - 100
                    distance=None,  # distance in cm
                    t=None,
                    finished=None,
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
            :paran finished: a function name passes as parameter that returns True if it is
                           supposed to run and False if it is finished.
            Examples:

                gyro.forward(50, distance=30, factor=0.005)

            """

            def forever():
            """
            In case we do not pass a finish function by name we
            just run forever.
                """

            return False

            if finish == None:
                finish = forever

            self.robot.reset()
            self.reset()
            while not finished():

              #
              # complete the body of the loop
              #

            self.robot.stop()  # stop the robot

