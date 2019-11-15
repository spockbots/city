#!/usr/bin/env pybricks-micropython
from spockbots.check import check
import time


def run_check():
    """
    Checks the robot by driving the large and medium motors and flashing the color sensors

    Order:

    * Large Motor left
    * Large Motor left
    * Medium Motor left
    * Medium Motor left
    * Color Sensor left
    * Color Sensor right
    * Color Sensor back

    """
    check()


if __name__ == "__main__":
    run_check()
