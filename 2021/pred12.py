class GO:
    def __init__(self, color = 0, width = 0, layer = 0):
        self._color = color
        self._width = width
        self._layer = layer
    
    def print(self):
        print('C:', self._color, 'W:', self._width, 'L:', self._layer)

#Derived class
class Point(GO):
    counter = 0

    def __init__(self, color = 0, width = 0, layer = 0, x = 0, y = 0):
        #Initialize members base class
        super().__init__(color, width, layer)

        #Initialize members of derived class
        self._id = Point.counter 
        self._x = x
        self._y = y
        Point.counter = Point.counter + 1
    
    def print(self):
        print(self._color)
        print('Point:')
        super().print()
        print(self._id, self._x, self._y)

class Line(GO):
    def __init__(self, color, width, layer, p1, p2):
        #Initialize  members of base class
        super().__init__(color, width, layer)

        #Initialize  members of derived class
        self._p1 = p1
        self._p2 = p2
    
    def print(self):
        print('Line:')
        super().print()
        self._p1.print()
        self._p2.print()

#Create graphic object
go = GO(1, 2, 3)
go.print()

#Create two points
p1 = Point(1,2,3, 15, 15)
p2 = Point(1,2,3, 27, 35)
p1.print()

#Create line
l1 = Line(1,2,3, p1, p2)
l1.print()