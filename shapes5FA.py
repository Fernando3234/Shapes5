#importing graphics pacakage
from graphics import *

#setting window size and window coordinates
shapesWin =GraphWin("Multiple Shapes", 800, 800)
shapesWin.setCoords(0, 0, 800, 800)

#First object          
rTri = Polygon(Point(1, 790), Point(10, 700), Point (200, 700))
rTri.setFill(color_rgb(220,30,20))
rTri.draw(shapesWin)

#Second object
rRectangle = Polygon(Point(790, 10), Point(700, 10), Point (700, 200), Point (790, 200))
rRectangle.setFill(color_rgb(220,30,20))
rRectangle.draw(shapesWin)

shapesWin.getMouse()
shapesWin.close()
