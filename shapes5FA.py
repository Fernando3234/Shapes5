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
bRectangle = Polygon(Point(790,10), Point(700, 10), Point (700, 200), Point (790, 200))
bRectangle.setFill(color_rgb(20,30,220))
bRectangle.draw(shapesWin)


#Third object
gOval = Oval(Point(790, 790), Point(600, 650))
gOval.setFill(color_rgb(20,220,20))
gOval.draw(shapesWin)

#fourth object
puCircle = Circle(Point(75, 100), 50)
puCircle.setFill(color_rgb(220,20,220))
puCircle.draw(shapesWin)

#fifth Object
blDiamond = Polygon(Point(350, 400), Point(400, 450), Point (450, 400), Point(400,350))
blDiamond.setFill(color_rgb(20,30,20))
blDiamond.draw(shapesWin) 


shapesWin.getMouse()
shapesWin.close()
