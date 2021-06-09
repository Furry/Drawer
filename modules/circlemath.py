from .graphics import Point
from math import sqrt

def hypotenuse(point1: Point, point2: Point):
    return sqrt(abs(point1.x - point2.x)**2 + abs(point1.y - point2.y)**2)
#END