#dieview2_color.py

from graphics import *
from random import randrange

class DieView2:
    """DieView is a widget that displays a graphical representation of a standard six-sided die."""

    def __init__(self, win, center, size):
        """Create a view of a die, e.g.: d1 = GDie(my Win, Point(40,50), 20) creates a die centered at (40,50) having sides of length 20."""

        #first define some standard values
        self.win = win
        self.background = "white"
        self.foreground = "black"  #color of the pips
        self.psize = 0.1*size      #radius of each pip
        hsize = size / 2.0         #half the size of the die
        offset = 0.6 * hsize       #distance from center to outer pips

        #create a square for the face
        cx, cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(p1,p2)
        rect.draw(win)
        rect.setFill(self.background)

        #Create 7 circles for standard pip locations
        self.pips = [ self.__makePip(cx-offset, cy-offset),
                      self.__makePip(cx-offset, cy),
                      self.__makePip(cx-offset, cy+offset),
                      self.__makePip(cx, cy),
                      self.__makePip(cx+offset, cy-offset),
                      self.__makePip(cx+offset, cy),
                      self.__makePip(cx+offset, cy+offset) ]

        #Create a table for which pips are on each value
        self.onTable = [ [], [3], [2,4], [2,3,4],
                         [0,2,4,6], [0,2,3,4,6], [0,1,2,4,5,6] ]
        self.setValue(1)
        #self.setColor("red")
        

    def __makePip(self,x,y):
        """Internal helper method a to draw a pip at (x,y)"""
        pip = Circle(Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setValue(self, value):
        """Set this die to display value."""

        self.value = value
        return self.value
    
        #Turn all the pips off
        for pip in self.pips:
            pip.setFill(self.background)

         #Turn the appropriate pips back on
        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)

       
        
                    

    def setColor(self, color):
        """sets the color of pips."""
        for pip in self.pips:
            pip.setFill(self.background)
        self.color = color
        self.value = self.setValue(self.value)
        for i in self.onTable[self.value]:
            self.pips[i].setFill(self.color)
        

            


        
