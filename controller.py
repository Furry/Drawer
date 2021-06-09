import modules.visualization

from modules.stepper import Stepper_28BYJ_48
from modules.circlemath import Point, hypotenuse

class Controller:
    def __init__(self):
        self.leftMotor = Stepper_28BYJ_48(16, 20, 21, 26)
        self.rightMotor = Stepper_28BYJ_48(17, 27, 22, 23)
        self.x, self.y = 0
    #END

    def moveTo(self, x: int, y: int):
        hypo1 = hypotenuse(Point(0, 0), Point(x, y))
        hypo2 = hypotenuse(Point(500, 0), Point(x, y))
    #END

    def at(self):
        return (self.x, self.y)
    #END