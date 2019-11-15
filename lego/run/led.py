#!/usr/bin/env pybricks-micropython

from spockbots.output import led, flash
import time


def run_led():
    """
    Test the LEDs
    """

    led("RED")
    time.sleep(0.2)
    led("GREEN")
    time.sleep(0.2)
    led("YELLOW")
    time.sleep(0.2)
    led("BLACK")
    time.sleep(0.2)
    led("WHITE")
    time.sleep(0.2)
    led("ORANGE")
    time.sleep(0.2)
    led("BLUE")
    time.sleep(0.2)
    led("BROWN")
    time.sleep(0.2)
    led("OFF")

    flash()


if __name__ == "__main__":
    run_led()
