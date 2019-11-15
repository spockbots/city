Coaches Disclaimer
==================

We have included in this document some information provided to the
kids in order to be transparent with the help and educational material
that has been issued to the team and to clearly distinguish
what ws done by coaches and what was done by the team.

We apologize for this long document, but we want to make sure we
communicate our activities properly to all.
However, the judges can skip this section and go directly to the
`Spockbots CIty` section.

The information in the coaches disclaimer has been collected by the
coaches, with some input from the team but in large part it has been
conducted just by the coaches as what we have done here is only needed
due to the evolving python mindstorm ecosystem. Naturally, in the
mindstorm GUI you do not have this issue as everything seems to be
stable there.

Team background
---------------

Most of the team members have extensive experience in the Mindstorm
EV3 GUI programming language. They developed for over more than 2 years a
library that includes:

* Gyro sensor based

  * turn
  * forward
  * reset with wait

* Color sensor based

  * calibration of multiple sensors while storing the failures in a file

    * using the calibrated minimum and maximum values for decisions if
      it is black and white

  * line following on black
  * line following on color
  * drive to black
  * drive to white
  * align to black
  * align to white

* One of the other strengths of the team was to build fancy attachments
  to their box robot they improved over the last two years.

So the team has an existing library and they could have made it easy
on themselves to just reuse this Mindstorm Myblocks library.


Choice of not using Scratch or Java
-----------------------------------

We shortly discussed using scratch and some of the kids do not like it
and instead wanted to use Python, as we used Python in the past on the
projects.  There was also no need to use Java as we could leverage the
kid's experience in python and focus on FLL learning tasks.

Choice of Python
----------------

The team came together and at discussed if to use Python or Mindstorm
GUI and it was decided as we already did Mindstorms to try out
Python. The team had in addition a vote a month back to decide if we
should switch back to the GUI as the python programming did not
progress as smoothly as expected. This is actually not related to the
kid's ability to learn and explore new things, but to subtle
differences between the GUI and Python, providing some unbalanced
advantage at this time still towards the GUI do to some administrative
functions that are included in the GUI that are not yet exposed or
corrected in the Python API.

Choice of the OS
----------------

During the project we have, with little input from the kids, experimented with
different operating systems and python versions.

Ev3dev, Visual Code and Python3

    Initially we selected ev3dev.org as the coach used that about 4-5
    years ago and contributed to the community a use case to run
    jupyter notebook services directly on the lego brick so students
    could use jupyter on their laptops to interactively use the robots
    via jupyter directly from the Laptops.  We however did not use
    this feature and instead started with Visual Code due to their
    ability to use a proper IDE instead of using notebooks.

    The student explored the features of interfacing in Python with
    the brick including focus on the build in line follower

    However the coaches made an executive decision not to use this
    version even after they updated to the snapshot releases due to
    two main issues: (1) we regularly observed that when something goes
    wrong the motor continue to operate; and due to the long start up
    time of python3 that made development too slow and cumbersome.

    The coaches explored advanced features such as a kill button via a
    thread and the use of an absolute drive function that is default
    in ev3dev but requires threading and python3 was needed.

    After however seeing the slow progress the students made while
    waiting too long for the programs to start.  The coaches mad the
    decision to use pybricks-micropython. At this time the team was
    asked if we should switch back to Mindstorm GUI, but it was
    decided to stick with Python as it a more educational goal for
    this team.

    In addition to these versions we also experimented with the
    releases for "stretch" and "buster" we used "buster", but learned later
    in the forums we should have used "stretch" due to issues with
    the overall reliability. However at that time we were more focused
    on speed of startup of python.

pybricks-micropython

    After experimenting with pybricks-micropython we found that the python
    loading time were significantly reduced.  We saw a significant
    increase in productivity as the kids could focus on programming
    and not on waiting for the program to get started. However, this
    OS and the python version is far less than ideal as it does not
    provide the more advanced features than the ev3dev OS provides. We also
    found that the micropython version of pybricks is faster than the
    one on ev3dev.

Pitfalls of Mindtstorm and Python
--------------------------------

In this section we document some of the pitfalls that we believe
should be considered to be fixed.

Runaway Motors

    (+) GUI: This does not happen in Mindstorm GUI giving it an
    advantage. Also the backspace button interrupts the program.

    (-) Python: We observed that in some cases when using ev3dev the
    motors simply run away and can not be made to stop. This seems to
    be discussed online as one of the open bugs.  A solution is posted
    in the ev3dev documentation but uses threads and can not be
    applied to all micropython versions. However, when applying this
    solution we sometimes still ended up in runaway motors.


Gyro Hardware Differences

    (+) GUI: The forums in the Internet have plenty of documentation
    on resetting the Gyros into a workable framework. This includes
    switching sensor modes, introducing timed loops and check for
    angles. Today it is easy for students to find them and copy them
    into their programs.  Our team simply used a delay of 0.1 seconds
    which was in most cases sufficient for our previous FLL
    participations.

    (-) Python: Due to the newness of python the reset is not properly
    discussed, furthermore, the reset into different senor modes
    although possible in the GUI requires elevated permissions in
    Python which gives the GUI an advantage as they do not have to
    learn how to become a system administrator in Linux ;-)

    (-) Problem for both: We had more than one robot and we found that
    we had some hardware issues with one of our Gyro sensors, as the
    reset did not function well. Without input from the kids we
    replaced this broken sensor with a new one. However the kids
    struggled for a long time trying to get that sensor to go until the
    coaches took a closer look at it and identified a hardware
    difference/fault. If we would not have had more than one robot we
    would not have been able to identify this and the team would still
    try to get the gyro to get working ;-) The interesting part was
    that just switching to a different sensor it worked much more
    reliable.

    In retrospect we found a significant set of documentation by one
    coach that discusses the difference between the many Gyro
    sensors. I think in python we see the same issue as discussed for
    the GUI version.

Motor Stall on Angle:

    (+) GUI: this isse does not occur in the GUI version and the motor
    returns after using a number of degrees or rotations within wait
    blocks.

    (-): Python: While driving forward for an angle or given rotation
    we find that sometimes the robot does not reach the given
    distance. Thus it may happen that the while loop may never
    end. What we found out is that the motors may gat stalled and
    never finish the loop. The fix to this is to also terminate if the
    motor has reached the angle minus a delta or if the gyro angle
    speed is 0. However, again we noticed that many times the gyro
    is not returning 0, but instead -1, so when we checked for the
    angle it also would not reliably terminate.

    We would like to see a better discussion of this issue in the
    manual as this is a feature that is not commonly discussed.

Light Sensor Blackout:

    (+) GUI: Although this error occurs also on the GUI version it seems that
    most programs that use a light sensor can recover from it quite easily

    (-) Python: Python is more strict and when we expect an integer but recieve
    an error during the reading of an unknown type, programs will no longer
    work -- we must write a special light sensor function that ignors this
    error and instead return a previous value

Program Loading Time:

    (-) GUI: the loading time is slow when the programs are big

    (-) Python3: The loading times seem even slower than using the GUI

    (-+) ev3dev micropython: Loading times seems slow, but ok

    (+) pybricks-micropython: Loading times are reasonable

    Times (need to be verified):

    * python3: 35 seconds
    * EV3DEVr micropython: 15 seconds
    * pybricks  micropython: 10 seconds
    * Bluetooth copy: 15 seconds
    * wireless copy: 3-5 seconds


Thread Support:

    (+) GUI: Threads are clearly better supported in the GUI via myblocks.
    Alone the graphical representation helps.

    (-) Python micropython: Threads do not seem to be properly supported.
    The official version of micropython points this out in its release notes.
    This should be made available.

OSX Bluetooth:

    (-) GUI: We had issues with reliability of the initial connection
    in macOS making bluetooth unusable for us. We verified this on
    different bricks and computers

    (+) Python: other than sometimes having to reboot the brick multiple
    times, bluetooth works much better in ev3dev

Documenting the Code:

    (+) GUI: The gui has some advanced features for documenting the
    code that are not available in Visual Code

    (++) Python: code documentation can be done in the source code and
    is easy to do

    (-) Python Sphinx: Python has superior functionality while using
    for example to document the code in Sphinx. However to enable this
    no proper documentation is provided or discussed in detail as far
    as we can tell. The coach wrote a code and Makefiles that allow
    the creation of the library in Sphinx.  However there was not
    enough time to teach the team how to do advanced features such as
    autodoc, code highlighting and inclusion and how to structure the
    document. We plan to do this in a future activity. However the
    programs and the contents have been created from templates that
    were provided as educational component given to the team. Using
    Sphinx did provide an advantage as the documentation nad code can
    be *snapshotted* easily and updates can be communicated quickly.
    We recommend that LEGO provides time to integrate such
    documentation feature ability into their upcoming documentation

    (-) Python Sphinx on the brick: The coaches experimented with
    generating the documentation on the brick directly, but it was
    just too slow, so a way was developed on how to generate them on a
    laptop.  This is beyond the need to know for the team.

    However the documentation can easily be created with

    `make html`
    `make pdf`

    These commands are executed by the coach on regular basis and not
    the team at this time. The commands create html and pdf documents

    (-) Google docs for python code documentation: Due to the advanced
    features of sphinx it seems cumbersome to use google docs if a
    system such as sphinx is able to generate a sophisticated
    documentation that fosters easier learning achievements.

SSH Key Management and Config:

    As the robots are in a secure area, they were not allowed to
    be put on WIFI. However, as we used Bluetooth we could overcome this
    issue. All robots were set up with ssh keys and ssh configs have been
    created to more easily log into the robots and identify them by color.
    This has been set up by the coach without input or knowledge of the team.

    This allows the team member to simply type

        `ssh blue`

    to log into the blue robot for example

    The resources provided by LEGO do not adequately describe how to change
    hostnames or how to setup ssh configurations while levaraging ssh-add.
    Naturally at this time this is a feature that is beyond the scope of a team.
    Instead LEGO could contribute programs that make the management of such
    tools trivial such as a commandline tool

        `mindstorm secure setup`

    or a button in Visual code that does this so inexperienced teams can
    also leverage this.
