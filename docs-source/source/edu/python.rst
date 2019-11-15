Python Essentials
=================

Variables
---------

Variables allow storing of data values. This is the same as
the EV3 GUI variable

Example::

    x = 5
    y = 10

Lists
-----

This is the same as the array in EV3 GUI.

Lists store multiple data values::

    vector = [x, y]
    vector = [5, 10]

Functions
---------

A function is a block of code which only runs when it
is called. It may return a value and can have parameters.
This is the same as a myblock, but easier to write and modify::

    def add(a,b):
        return a + b

    def PRINT(message):
        print("Message", message)

Classes
-------

With classes we can group functions and variables conveniently into an object.
An object is just like a variable that uses the class as template. We can refer to
all variables and functions on this object. Functions in a class are called methods.
A special method is __init__ which is called once when we declare an
object from the template::

    class Person:

        def __init__(name, age, weight):
            self.name = name
            self.age = age
            self.height = height

        def grow(amount):
            self.height = height + amount

        def how_tall():
            return self.height

    sandra = Person("Sandra", 14, 150)
    sandra.grow(1)
    print (sandra.height)      #  151
    print (sandra.how_tall())  #  151


Conditions
----------

Conditions allow us to react if a value is true or false. It is the same
as in EV3 GUI but easier to write::

    if sandra.height > 180:
        print("He is tall")
    elif sandra.height < 180:
        print("He is still growing")
    else:
        print("he is exactly 180cm")

Loops
-----

We used while and for loops to repeat an indented block of code. While loops can
also easily loop over elements in a list.

Loop forever
~~~~~~~~~~~~

::

    while True:
        print("I loop forever")

Loop with condition
~~~~~~~~~~~~~~~~~~~~

::

    counter = 1
    while counter <= 3:
        print (counter)
        counter = counter + 1

    # 1
    # 2
    # 3

Loop with break
~~~~~~~~~~~~~~~

::

    counter = 1
    while True:
        print (counter)
        counter = counter + 1
        if counter > 3:
           break # break leaves the loop

    # 1
    # 2
    # 3

Loop through a list
~~~~~~~~~~~~~~~~~~~

::

    for counter in [1,2,3]:
        print (counter)

    # 1
    # 2
    # 3

Exceptions
----------

When working with the Mindstorm sensors we sometimes find that the sensors
do not work properly and return no result. Python has a special mechanism
for this that is called try/except. Let us illustrate this.

Let us simulate a sensor with a fault that we can set that returns an
error if we pass the parameter value 1 but returns its value for all other inputs::

    def sensor(number):
        if number == 1:
            rasie ValueError # this just creates an error
        else
            return number

Now we can simulate a faulty sensor and deal with its exceptions.
Let us test the sensor in a loop such as::

    last_value=0 # we set a last value
    for number in [0,1,2]:
        try: here we try to see if the function works
            value = sensor(number)
            last_value = value  # stores the last value and when
                                # an exception occurs we read that
            print("Success:", number)
        except:
            value = last_value
            print("Error:", value)

The nice thing with this loop is that not only do we know when there is
an error, but we correct the error with just the last value we found

The result is::

    Success: 0
    Error: 1
    Success: 2

This is naturaly helpful in cases of the Light sensors, when once in a while the
light sensor value dos not return properly.

Function as a parameter
-----------------------

The Mindtsorm GUI has a convenient Wait method and loop exits that probe certain conditions.
Python does not directly provide them, but allows you to create loops.

Instead of just testing for a condition such as introduced in the previous sections,
we can also use a functionname as a parameter.

Let us demonstrate and assume that the function

* motor.angle() - returns the angle of the angle of the gyro


we can now create a test function such as

::

    def run_for_a_distance(): # is true for running
        return motor.angle() <= 1000

This allows us now to define a function that contains a loop to which we pass the running() condition:

::

    def followline(speed, until=None):

        while until():
            print("I am following the line ")
            time.sleep(0.1)

Now we can call it just as follows

::

    followline(25, run_for_a_distance)

The convenient thing now is that we can create other functions so we
do not have to rewrite the function that loops but just change the termination
function such as

::

    def run_till_black(): # is true for running
        return colorsensor.reflection() > 10

and run it with

::

    followline(25, run_till_black)


Import
------
When we create code in separate files they can be made known within a
program while importing the functions, classes, or variables. This
allows us to organize the code while grouping topical code into a file.

::

    from spockbots.motor import SpockbotsMotor
    from time import sleep

Program
-------

A program can be executed in a terminal on the EV3 brick. It must be executable.
Let us assume the following core it in the file `run_led.py`.
we make it executable with::

    chmod a+x run_led.py

Here is an example::

    #!/usr/bin/env pybricks-micropython

    from spockbots.output import flash
    import time


    def run_led():
        """
        Flashes the LEDs on the brick
        """

        flash()


    if __name__ == "__main__":
        run_led()

The first line tells us to use Python to run the program.

The if `__name__` line tells us to run the next lines (e.g. the function)
as functions are not run when we simply define them.

Advanced Python
===============

.. warning:: The language features in the `Advanced Python section have not been taught to the team.

Decorators
----------


In some cases it is convenient to augment function calls with debug
messages or functionality when we call the method.  Instead of adding
the same code to all the functions we could use python decorators that
we put above the functions.  Here are some convenient decorators such
as printing in a debug decorator the start and name of the function
and at the end the end and name.



::

    def debug(f):
        print("Start", f.__name__)
        return f
        print("End", f.__name__)

    def killable(f):
        if not check_kill_button(self):
            return f

    def message(msg):
        print(msg)
        return lambda f:f

To use such decorators you can place them on top of the method or function definition preceeded by a `@` character::

    # plain decorator
    @debug
    def f():
        print("I am f")

Lets do an an advanced decorator that is very useful for the robot, e.g. a kill button. The kill button is explained
in the lessons section in more detail and you need to explor that first before you can use this decorator. We will
provide a robot centric example in near future.::


    @killable
    def g():
        print("I am g")

You can combine decorators. Please note that the order matters::

    @debug
    @killable
    def g():
        print("I am g")


You can use the decorator with arguments as follows::

    @message('Testing')
    def h():
        print("I am h")


You can even use decorators for classes::

    # decorator of class
    @debug
    class A:
        pass




Threads
-------

.. warning:: Threads are not supported in pybricks as far as we can tell. Proper documentation to that is missing.
If it is it looks something like::

    from threading import Thread
    import sys
    from time import sleep

    def killbutton():
        while True:
            # complete this example
            # if button pressed than
            #       break
        # kill the motors (not shown here)
        print("KILL")
        sys.exit()

    killwait = Thread(target=killbutton)
    killwait.start()

    while True:
        print("Wait for kill")
        sleep(0.5)
