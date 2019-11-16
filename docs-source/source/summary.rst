Summary of Robot Features
=========================

Mechanical Design
-----------------


**Durability** - Robot designed to maintain structural integrity and have the ability to withstand
rigors of competition

* We build a box robot that contaons a frame around it that is stable
* The robot is durable and can withstand drops
* The cables are out of the way

**Mechanical** - Efficiency Robot designed to be easy to repair, modify, and be handled by technicians

* The robot does not need to be repaired a lot due to its sturdy design

**Mechanization** - Robot mechanisms designed to move or act with appropriate speed, strength and
accuracy for intended tasks (propulsion and execution)

* The robot has 63.6 mm wheel which allows to go fast, but also precise.
* The robot has 2 medium motors built in that allow for easy attachments.

Programming
-----------

**Programming Quality**  Programs are appropriate for the intended purpose and should achieve consistent
results, assuming no mechanical faults

* We tested several runs and they were 100% reliable given our goals for the mission.
* We use functions to describe the runs so they can be quickly developed

**Programming Efficiency** Programs are modular, streamlined, and understandable

* We use classes for Colorsensors and motors
* We use a lot of functions and methods
* We use seperate programs for runs
* The code is very modular
* The code is documented
* We use a python document generator to create the documentation.

**Automation/Navigation** - Robot designed to move or act as intended using mechanical and/or sensor
feedback (with minimal reliance on driver intervention and/or program timing)

* We use 3 color sensors
* We use 1 gyro sensor
* We use line following
* We programmed our own left, right, based on angle rotations for the motor
* We use Gyro sensor left, right, forward
* We use color and reflective mode to identify markers to react
* We make sure the robot is not running too fast if we run into the crane
* We make sure the robot is fast when we turn over the lift
* We can use our line following forwards and backwards, by inverting the motors
* All reflective light values are independently calibrated and mapper between 0 to 100
* We have a special interrupt

Strategy and Innovation
------------------------

**Design Process**  Developed and explained improvement cycles where alternatives were considered
and narrowed, selections tested, designs improved (applies to programming as
well as mechanical design)

* Programming - we focused on python and explored if we can replicate our library which we previously developed in
Mindtsorm. This was new to us and we were not sure if we can do the missions in Pythoin. We found out we can.

* Mechanical design - we designed a number of robots. we found that its bets to place the brick over
  the wheels as otherwise the wheels slip

* We tried mechanical attachments that showed they were to heavy and the robot spipped. We even tried wider wheels but
  they also slipped.

* We made all atatchments very light and relatively small.

* The attachments are custom designed for the missions

* We can drive backwards to drive up the ramp. The light sensor that is than
  facing the ramp is high up so its possible to go up the ramp.

**Mission Strategy** Clearly defined and described the team's game strategy

* Our main goal was to learn python and test various functionssuch as line following, gyro, movements
* We picked missions that were easy to do but give us some number of points

  .. warning:: TODO: list of missions with their points

**Innovation** - Team identifies their sources of inspiration and creates new, unique, or
unexpected feature(s) (e.g. designs, programs, strategies or applications) that are
beneficial in performing the specified tasks

* The bets feature is the calibration of the light sensor that drives ove a line and stores
  the minimum black and maximum white value. Than we use a special sensor value function to always return
  values mapper between 0 and 100.
* We reimplemented turn, left and right with motor angle measuremnts
* We have implemented line following
* We have implemented a gyro go straight
* All of the modular code is reusable and could be used by others.

