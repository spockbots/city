Python
======

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
an object is just like a variable that uses the class as template. we can call
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

    seric = Person("Seric", 14, 150)
    seric.grow(1)
    print (seric.height)      #  151
    print (seric.how_tall())  #  151


Conditions
----------

Conditions allow is to react if a value is tru or false. It is the same
as in EV3 GUI but easier to write::

    if seric.height > 180:
        print("He is tall")
    elif seric.height < 180:
        print("He is still growing")
    else:
        print("he is exactly 180cm")

Loops
-----

We used while and for loops the repeat an indented block of code. While loops can
also loop over elements in a list easily.

### Loop forever

::

    while True:
        print("I loop forever")

### Loop with condition

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

    for counter in [1,2,3]:
        print (counter)

    # 1
    # 2
    # 3

Import
------
When we create code in separate files they can be made known within a
program while importing the functions, classes, or variables. This
allows us to organize the code while grouping topical code into a file.

::

    from spockbots.motor import SpockbotsMotor
    from time import sleep

## Program

A program can be executed in a terminal on teh EV3 brick. It must be executable.
Let us assume the following core it in the file `run_led.py`.
we make it executable with::

    chmod a+x run_led.py

Here an example::

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

The first line tells us to use python to run the program.

The if __name__ line tesll us to run the next lines (e.g. the function)
as functions are not run when we define them.



