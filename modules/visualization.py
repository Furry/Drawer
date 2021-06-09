from .graphics import *
from .circlemath import hypotenuse

def draw(obj):
    obj.draw(win)
#END

def drawRed(obj):
    obj.setOutline("red")
    obj.draw(win)
#END

def drawBlue(obj):
    obj.setOutline("blue")
    obj.draw(win)
#END

win = GraphWin(width=505, height=500, autoflush=True)

point1 = Point(5, 5)
point2 = Point(500, 5)
point3 = Point(250, 250)

mousePos = [25, 25]
def mouseMove(event):
    if event.x != None:
        mousePos[0] = event.x
        mousePos[1] = event.y
    #END
#END

win.bind("<Motion>", mouseMove)

def mouseMovement():

    for item in win.items[:]:
        item.undraw()
    win.update()

    point3 = Point(mousePos[0], mousePos[1])

    # Base Connection Lines
    draw(Line(point1, point2))
    draw(Line(point2, point3))
    draw(Line(point1, point3))

    # Y Axis Connection Line
    drawRed(Line(point3, Point(point3.x, point1.y)))

    # Calculate Hypotenuse
    triangle1 = hypotenuse(point1, point3)
    triangle2 = hypotenuse(point2, point3)

    # Main Nodes
    draw(Circle(point1, 3))
    draw(Circle(point2, 3))
    drawRed(Circle(point3, 3))

    # Bounds
    drawBlue(Circle(Point(5, 5), triangle1))
    drawBlue(Circle(Point(500, 5), triangle2))
#END


while True:
    mouseMovement()
    time.sleep(.05)
#END

