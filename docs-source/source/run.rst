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
  We use the balck lines and that allow us to be more precise.

Mechanical
  We have an attachment designed that pushes the house block, a lever that starts the swing, a
  lever that allows us to flip a blue stand
  and a lever tu turn the elevator.

Mission Order
  THis mission would be best to be strarte at the begining as it is mor complex to set up
  the the crane, but the crane may swing so we decided to run the swing first.


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
  There is a balck line that we can allign the blue peg with.

Run
  We use the balck line to align the robot so that the attachment is working well.

Mechanical
  We have an attachment designed that pushes the block and activates the
  blue levers at the righ time. The drive must not be fast into the crane. The crane block
  must not swing wne  we start.

Mission Order
  To avoid the swinging of the line (by other teams moving the table), this is our first mission.


run.tan_circle
-------

.. automodule:: run.tan_circle
   :members:
   :undoc-members:
   :show-inheritance:

run.red_circle
-------

.. automodule:: run.red_circle
   :members:
   :undoc-members:
   :show-inheritance:

run.black_circle
-------

.. automodule:: run.black_circle
   :members:
   :undoc-members:
   :show-inheritance:
