#Bartosz Kosakowski
#400028494
#Lab 4 Question 3
####################
from math import pi

class Shape:
    def set_origin(self, x, y):
        self.x, self.y = x, y
    def move(self, dx, dy):
        """Move by dx and dy"""
        self.x, self.y = self.x+dx, self.y+dy

class Line(Shape):
    def __init__(self, x, y, u, v):
        """Line with start point (x, y) and end point (u, v)"""
        Shape.set_origin(self, x, y)
        self.u, self.v = u, v
    def move(self, dx, dy):
        Shape.move(self, dx, dy)
        self.u, self.v = self.u+dx, self.v+dy
    def __str__(self):
        return "Line from ("+str(self.x)+", "+str(self.y)+ \
               ") to ("+str(self.u)+", "+str(self.v)+")"
    def area(self):
        return 'Line with an area of 0'

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        """Rectangle at (x, y) with width w and height h"""
        Shape.set_origin(self, x, y)
        self.w, self.h = w, h
    def __str__(self):
        return "Rectangle at ("+str(self.x)+", "+str(self.y)+ \
               "), width "+str(self.w)+", height "+str(self.h)
    def area(self):
        return 'Rectangle with an area of ' + str(self.w * self.h)

class Group:
    def __init__(self):
        self.c = set()
    def add(self, s):
        """Add shape s to group"""
        self.c = self.c|{s}
    def move(self, dx, dy):
        """Move by dx and dy"""
        for s in self.c:
            s.move(dx, dy)
    def __str__(self):
        r = "Group with:"
        for s in self.c:
            r = r+"\n  "+str(s)
        return r
    def area(self):
        self.areaGroup = 0
        for s in self.c:
            self.areaGroup = self.area + s.area
        return self.areaGroup
            

#-=-=-=-=-=-=NEW CODE=-=-=-=-=-=-=-
class Circle(Shape):
    def __init__(self,x,y,r):
        Shape.set_origin(self,x,y)
        self.r = r
    def __str__(self):
        return "Circle at ("+str(self.x)+", "+str(self.y)+ \
               "), radius "+str(self.r)
    def area(self):
        return 'Circle with an area of ' + str(pi*(self.r)**2)


    
class Polygon(Shape):
    def __init__(self,polyCoords):
        Shape.set_origin(self,polyCoords[0][0],polyCoords[0][1])
        self.poly = polyCoords
    def __str__(self):
        return 'Polygon with ' + str(self.poly)
    
    def area(self):
        self.polyArea = 0
        for i in range(len(self.poly)-1):
            self.polyArea = self.polyArea + (self.poly[i][0]*self.poly[i+1][1] - self.poly[1+1][0]*self.poly[i][1])
        return 'Polygon with an area of ' +str(0.5 * self.polyArea)
    
    def move(self,dx,dy):
        self.polyList = []
        for i in range(len(self.poly)):
            self.polyList.append(list(self.poly[i]))
            self.polyList[i][0] = self.polyList[i][0] + dx
            self.polyList[i][1] = self.polyList[i][1] + dy
        self.poly = tuple(self.polyList)
        return self.poly

g = Group()
l = Line(1, 2, 5, 6); g.add(l)
c = Circle(1,-5,1); g.add(c)
r = Rectangle(-2, -3, 2, 3); g.add(r)
p = Polygon([(0,0),(4,0),(2,2),(4,4),(0,4),(2,2)]); g.add(p)
print(g)
g.move(1, 1)
print(g)

