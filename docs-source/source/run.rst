City Runs
=========

run.check
---------

.. automodule:: run.check
   :members:
   :undoc-members:
   :show-inheritance:

run.calibrate
-------------

.. automodule:: run.calibrate
   :members:
   :undoc-members:
   :show-inheritance:



run.swing
---------

.. automodule:: run.swing
   :members:
   :undoc-members:
   :show-inheritance:

.. literalinclude:: ../../lego/run/crane.py
   :language: python


**Reliability**:

Setup
  To help the setup we are using a jig.

Run
  We use the black lines and that allow us to be more precise.

Points
  Including the "advantage" points for containing all parts in the small home,
  we can score a maximimum of 90 points on this run.

Mechanical
  We have an attachment designed that pushes the house block, a lever that starts the swing, a
  lever that allows us to flip a blue house stilt
  and a lever to flip the elevator.

Mission Order
  This mission would be best to be start at the begining as it is more complex to set up
  than the crane, but the crane may fall off so we decided to run the swing first.


run.crane
---------

.. automodule:: run.crane
   :members:
   :undoc-members:
   :show-inheritance:

.. literalinclude:: ../../lego/run/crane.py
   :language: python


.. list-table::

    * - .. figure::  images/crane-setup.png

           Crane 1. Crane setup does not have to be precise

      - .. figure:: images/crane-setup-2.png

           Crane 2. Crane setup still works well when the peg points to the line.

      - .. figure:: images/crane.png

           Crane 4. Successful placement

**Reliability**:

Setup
  The setup for the crane mission is important, but it does not have to be precise.
  There is a balck line that we can align the blue peg with.  There is no jig for
  this run.

Run
  We use the black line to align the robot so that the attachment is working well.

Points
  If the blue blocks stack properly, we will earn 50 points, plus the 5 point
  "advantage" bonus for fitting in the small home.

Mechanical
  We have an attachment designed that pushes the block and activates the
  blue levers at the righ time. The drive must not be fast into the crane. The crane block
  must not swing wne  we start.

Mission Order
  To avoid the swinging of the line (by other teams moving the table), this is our first mission.


run.black_circle
-------

.. automodule:: run.black_circle
   :members:
   :undoc-members:
   :show-inheritance:

Setup
  We use the grid in the starting section to align and aim the robot.

Run
  We just send the robot forward 48cm using the gryo, then back up 48cm back to base.

Points
  If the building is entirely in the circle we score 40, plus the 5 point
  mission bonus for all attachments in the small home.

Mechanical
  We use a simple and light building holder attachment that shoves the building
  to the circle.

Mission Order
  This run is done after the crane.


run.red_circle
-------

.. automodule:: run.red_circle
   :members:
   :undoc-members:
   :show-inheritance:

Setup
  We use our standard jig to align the robot at the correct angle

Run
  We send the robot forward 59cm using the gryo, then turn left 40 degrees,
  then forward another 3cm.  Then reverse 10cm, turn left 45 degrees, and back 70cm
  to base.

Points
  If the building is entirely in the circle we score 50, plus the 5 point
  "advantage" bonus for all attachments in the small home.

Mechanical
  We use a simple and light building holder attachment that shoves the building
  to the circle.

Mission Order
  This run is done last, after the black run.

run.tan_circle
-------

.. automodule:: run.tan_circle
   :members:
   :undoc-members:
   :show-inheritance:

Setup
  We use our standard jig to align the robot at the correct angle

Run
  We send the robot forward 85cm using the gryo, then turn left 50 degrees,
  then forward 25cm.  Then reverse 10cm, turn right 50 degrees, and back 120cm
  to base.

Points
  If the building is entirely in the circle we score 45, plus the 5 point
  "advantage" bonus for all attachments in the small home.

Mechanical
  We use a simple and light building holder attachment that shoves the building
  to the circle.

Mission Order
  This is an optional run if we have time.

