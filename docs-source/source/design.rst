Design
======

Goals for using Python
----------------------

Our main goal this year was to learn Python.

Previously we used Mindstorms GUI and developed a sophisticated library with many myblocks.

Questions

#. Can we convert this library into python?

#. Would python easier than the mindstrom GUI?

#. Would it be easier to define missions with Python?

#. Would the robot perform well with the Python program?

#. What general reasosn are there for and against Python?

Previous Mindstorm GUI programs

* We had an library developed in Mindstorm GUI with
  many myBlocks that we used previously to develop code.
  Can they be redeveloped in Python?

* We had some issues with using Bluetooth between Mac
  and the robot in Mindstorm. Is this improved in Python

* In contrast to Windows, the GUI on Mac seems slower.
  Is the development in python faster?

* We often ran out of screen space as the programs were long.
  Does using python help?

* We had some issues with the Gyro and light sensors
  in the mindstor GUI. Do these issues occur also in python?


.. list-table:: Mindtsorm GUI Issues
   :widths: 20 10 35 35
   :width: 100
   :header-rows: 1

   * - Task
     - Winner
     - Mindstorm
     - Python
   * - Bluetooth on Mac
     - Python
     - Connection could often not be done easily
     - No issues
   * - MyBlocks definition
     - Python
     - Complicated to define, if you make an error in
       the parameters one needs to start over.
     - With functions easy to define and correct
   * - Gyro Drift
     - Neither
     - Gyro needs to be plugged in and out to avoid drift
     - Gyro needs to be plugged in and out to avoid drift
   * - Gyro Reset
     - Neither
     - Reset requires a time delay
     - Reset requires a time delay.
   * - Color Sensor No value
     - Python
     - Sometimes the color sensor has no value.
       We did not have a fix for that.
     - Easy to fix in python while using the previous value.
       Comes back quickly
   * - Color Sensor reset with mor than one sensor
     - Python
     - Not available
     - We implemented this so that all color sensors return always values
       between 0 -100, this helps line following.
   * - Editor
     - Equal
     - GUI is intuitive to undertand but has issues with myblock. Limited space, myblocks do not have names unerd them
     - Visual code is easy a bit mor complex to understand, but once you know it writing programs is easy.
       Upload and run code with F5 is convenient

Overall winner:

    Python

What should be added to Python:

    * Color Sensor calibration and value code we developed that returns values between 0-100 for all sensors
    * A test to see if the gyro is drifting
    * A solution to avoid the unplugging of the gyro sensor

Observations and answers:

  Gyro:

  1. The gyro needs to be plugged in and out at the beginning
     to avoid drifting.

     This could not be solved in Python but we implemented a function that
     detects better if the Gyro drifts.

  2. We need to have a wait till the Gyro is calm

     We reimplemented this not with  time delay, but a counter to see if
     the angle has changed. This could also be implemented in mindstorm GUI

  Light Sensor:

  1. sometimes the light sensor did not return a result
  2. We developed a calibration that drove over a line to
     calibrate our sensors. However, the reset block is only
     designed to use one Gyro and not 2




Mechanical Design
-----------------

* TBD

