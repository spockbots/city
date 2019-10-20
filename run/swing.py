import spockbots.robot as robot

def run_swing():

    robot.led("LEFT", "YELLOW")
    robot.led("RIGHT", "YELLOW")
    robot.beep()
