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

#. What general reasons are there for and against Python or Mindstorm?

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


.. list-table:: Python and Mindtsorm GUI comparison
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
     - GUI is intuitive to understand but has issues with myblock. Limited space, myblocks do not have names under them but just icons
     - Visual code is easy but a bit mor complex to understand, but once you know it writing programs is easy.
       Upload and run code with F5 is convenient
   * - Interrupting a wrong program with the backspace button
     - Mindstorm
     - This can easily be done in mindstorm
     - This does not work in python. We need to add code for that
   * - Younger Kids
     - Mindstorm
     - Mindstorm GUI is intuitive, but best for small programs
     - Python is a more difficult to learn by younger kids
   * - Older Kids
     - Python
     - Mindostom GUI becomes cumbersome when we develop more complex programs
     - Python is easy to learn by older kids

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

