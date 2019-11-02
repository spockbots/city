
def followline_1(t=2, port=2, speed=50, factor=2, black=0, white=100):
    midpoint = (white - black) / 2 + black

    end_time = time.time() + t
    while end_time > time.time():

        value = light(port)

        position = motor_left.position
        print(position)

        if value > midpoint:
            motor_left.on(SpeedPercent(speed))
            motor_right.on(SpeedPercent(int(speed / factor)))
        else:
            motor_left.on(SpeedPercent(int(speed / factor)))
            motor_right.on(SpeedPercent(speed))
    motor_left.off()
    motor_right.off()


def followline_2(t=2, port=2, speed=25, black=0, white=100, kp=0.3):
    midpoint = (white - black) / 2 + black

    current = time.time()
    end_time = current + t

    #	while True:

    print("AAA", end_time, current)
    while current < end_time:
        value = light(port)
        position = motor_left.position
        print(current, position, value)

        correction = kp * (midpoint - value)

        steering.on(-correction, speed)

        # steering.on(correction, speed)
        current = time.time()
    steering.off()


def followline_3(t=2, port=2, speed=25, black=0, white=100,
                 kp=1.0, ki=1.0, kd=1.0):
    integral = 0

    midpoint = (white - black) / 2 + black
    lasterror = 0.0

    current = time.time()
    end_time = current + t

    while current < end_time:
        value = light(port)

        error = midpoint - value
        integral = error + integral
        derivative = error - lasterror

        correction = kp * error + ki * integral + kd * derivative

        print(correction)

        steering.on(-correction, speed)

        lasterror = error
        current = time.time()
    steering.off()


def followline_5(t=2, port=3, speed=25, black=0, white=100, delta=-35, factor=0.7):
    current = time.time()
    end_time = current + t

    if moves_forward:
        f = 1.0
    else:
        f = -1.0

    while current < end_time:
        value = light(port)

        correction = delta + (factor * value)
        correction = f * correction

        print(correction)

        steering.on(correction, speed)

        current = time.time()
    steering.off()


def followline_4(t=3.0, port=3,
                 speed=25,
                 black=0, white=100,
                 kp=3.0, ki=0.01, kd=0.0):
    tank.cs = colorsensors.colorsensor[port].sensor
    try:
        tank.follow_line_debug(
            target_light_intensity=None,
            kp=kp, ki=ki, kd=kd,
            speed=SpeedPercent(speed),
            white=60,
            follow_for=follow_for_ms,
            ms=t * 1000
        )
    except Exception:
        tank.stop()
        raise


def followline_6(run=True, steering=15, speed=10, black=15, port=2):
    """
    Follows the line on a given port.
    run is a True-False function.
    If its true it continues.
    If its falls it stops

    Example:

    robot.followline_simple(robot.forever())

    """
    # this needs to be replaced with the spockbots color sensors

    while run:
        value = colorsensors.value(port)
        print(value)
        if value < black:
            tank.on(-steering, SpeedPercent(speed))
        else:
            tank.on(steering, SpeedPercent(speed))
    stop()


def followline_simple(run=True, steering=15, speed=10, black=15, port=2):
    """
    Follows the line on a given port.
    run is a True-False function.
    If its true it continues.
    If its falls it stops

    Example:

    robot.followline_simple(robot.forever())

    """
    # this needs to be replaced with the spockbots color sensors

    while run:
        while colorsensors.value(port) < black:
            tank.on(SpeedPercent(speed), SpeedPercent(2 * speed))
        while colorsensors.value(port) > black:
            tank.on(SpeedPercent(2 * speed), SpeedPercent(speed))
    stop()
