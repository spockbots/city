class Motor:

    def __init__(self, port, direction=None, gears=None): pass

    def dc(self, duty): pass
    def angle(self): return 0.0
    def speed(self, )  : return 100.0
    def stop(self, stop_type=None)  : pass
    def run(self, speed)  : pass
    def run_time(self, speed, time, stop_type=None, wait=True)  : pass
    def run_angle(self, speed, rotation_angle, stop_type=None, wait=True)  : pass
    def run_target(self, speed, target_angle, stop_type=None, wait=True)  : pass
    def track_target(self, target_angle)  : pass
    def stalled(self, )  : pass
    def run_until_stalled(self, speed, stop_type=None, duty_limit=None)  : pass
    def set_run_settings(self, max_speed, acceleration)  : pass
    def set_pid_settings(self, kp, ki, kd, tight_loop_limit, angle_tolerance, speed_tolerance, stall_speed, stall_time): pass
    def reset_angle(self, angle): pass

class TouchSensor():
    def __init__(self, port): pass
    def pressed(self): pass

class ColorSensor():
    def __init__(self, port): pass
    def color(self): return 100
    def ambient(self): return 100
    def rgb(self): pass
    def reflection(self): return 0

class InfraredSensor():
    def __init__(self, port): pass
    def distance(self): pass
    def beacon(self, channel): pass
    def buttons(self, channel): pass

class UltrasonicSensor():
    def __init__(self, port): pass
    def distance(self, silent=False): pass
    def presence(self): pass
    def speed(self): pass
    def angle(self): pass
    def reset_angle(self, angle): pass

class GyroSensor():
    def __init__(self, port, direction=None): pass
    def speed(self): pass
    def angle(self,): pass
    def reset_angle(self,angle): pass
