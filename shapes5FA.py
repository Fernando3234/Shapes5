#importing graphics pacakage
from graphics import *

#setting window size and window coordinates
rTriWin =GraphWin("Multiple Shapes", 800, 800)
rTriWin.setCoords(0, 0, 800, 800)

#First object         
rTri = Polygon(Point(10, 790), Point(10, 700), Point (200, 700))
rTri.setFill(color_rgb(220,30,20))
rTri.draw(rTriWin)
                                                                     
rTriWin.getmouse()
rTriWin.close()

                 
