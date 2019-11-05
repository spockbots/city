

#######################################################
# Turn
#######################################################

def turn(speed, angle):
    """
    takes the radius of the robot and dives on it for a distance based on the ancle
    :param speed:
    :param angle:
    :return:
    """
    reset_motors()

    c = axle_track * math.pi
    fraction = 360.0 / angle
    d = c / fraction
    a = distance_to_angle(d) / 10.0

    left_motor.run_angle(speed * 10, -a, Stop.BRAKE, False)
    right_motor.run_angle(speed * 10, a, Stop.BRAKE, False)

    while abs(left_motor.angle()) < abs(a) and abs(left_motor.angle()) < abs(a):
        pass
    stop()


#######################################################
# Line
#######################################################

def followline(
        speed=25,  # speed 0 - 100
        t=None,  # time in seconds
        distance=None,  # distance in cm
        port=3,  # the port number we use to follow the line
        right=True,
        black=0,  # minimal balck
        white=100,  # maximal white
        delta=-35,  # paramaters to control smoothness
        factor=0.7):  # parameters to control smoothness

    print (distance)

    if right:
        f = - 1.0
    else:
        f = 1.0

    current = time.time()  # the current time
    if t is not None:
        end_time = current + t  # the end time

    reset_motors()

    while True:
        value = light(port)  # get the light value

        # correction = delta + (factor * value)  # calculate the correction for steering
        correction = f * factor * (value + delta)
        # correction = f * correction  # if we drive backwards negate the correction

        on(speed, correction)  # switch the steering on with the given correction and speed

        current = time.time()  # measure the crurrent time

        # if the time is used we set run to false once the end time is reached
        # if the distance is greater than the position than the leave the
        angle = left_motor.angle()

        traveled = angle_to_distance(angle)

        print(correction, angle, traveled)

        if t is not None and current > end_time:
            break  # leave the loopK
        if distance is not None and distance < traveled:
            break  # leave the loop

    stop()  # stop the robot


#######################################################
# Setup
#######################################################


def gotoblack(speed, port, black=10):
    """
    The robot moves to the black line while using the sensor on the given port

    :param speed: The speed
    :param port: The port 2,3,4
    :param black: The value to stop
    """
    on(speed, 0)
    while  light(port)  > black:
        pass
    stop()


def gotowhite(speed, port, white=90):
    """
    The robot moves to the white line while using the sensor on the given port

    :param speed: The speed
    :param port: The port 2,3,4
    :param white: The value to stop
    """

    on(speed, 0)
    while light(port) < white:
        pass
    stop()


#######################################################
# Setup
#######################################################
def setup():
    pass
    # beep()
    # sound()


    # led(None, "RED")
    # led(None, "GREEN")
    # led(None, "YELLOW")
    # flash()

    # clear()
    # Print("Hallo")
    # Print("World")
    # voltage()



    forward(25, 10)
    #time.sleep(1)
    turn(25, 45)
    #time.sleep(1)
    forward(25, 30)
    #time.sleep(1)


    turn(25, -50)
    #time.sleep(1)
    forward(25,10)
    #time.sleep(1)

    # gotowhite(25, 3)
    # gotoblack(10, 3)
    # gotowhite(10, 3)
    #forward(5, 2)
    #forward(-20, 20)

    # turn(20, 45)
    # forward(-75, 60)
    # sleep(2)

    #followline(speed=20, distance=30)