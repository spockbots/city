from ev3dev2.wheel import Wheel

STUD_MM = 8

class SpockbotsRim(Wheel):
    """
    Wheel 43.2mm D. x 18mm (flush axle stem)
    Part Number: 86652
    """
    def __init__(self):
        Wheel.__init__(self, 43.2, 18)


class SpockbotsTire(Wheel):
    """
    Wheel 62.4 x 20 with Short Axle Hub, with Black Tire 62.4 x 20
    Part NUmber: 32019
    """

    def __init__(self):
        Wheel.__init__(self, 62.4, 20)