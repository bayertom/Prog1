from copy import deepcopy
from math import *
from operator import attrgetter

class GO:
    def __init__(self, color = 0, level = 0, width = 0):
        self._color = color
        self._level = level
        self._width = width

    #Property nebo gettery/settery
    def print(self):
        print("Color = " + str(self._color) + ", Level = " + str(self._level) + ", Width = " + str(self._width))

#Odvozeni od GO
class Point(GO):
    #Datova polozka tridy
    counter = 0

    #Inicializator
    def __init__ (self, color = 0, level = 0, width = 0, x = 0, y = 0):
        #Inicializator GO
        super().__init__(color, level, width)

        #Datove polozky objektu
        self.__id = Point.counter
        self.__x = x
        self.__y = y

        #Inkrementace datove polozky tridy
        Point.counter = Point.counter + 1

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    def print(self):
        print("\nPoint, attributes + geometry:")
        super().print()
        print(str(self.__id), str(self.__x), str(self.__y))

    #Define operators <, >, ==
    def __lt__(self, other):
        return self.__x < other.__x
    
    def __gt__(self, other):
        return self.__x > other.__x

    def __eq__(self, other):
        return (self.__x == other.__x) and (self.__y == other.__y)

#Distance function
def dist(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return (dx*dx + dy*dy)**0.5

#Polymorphism
go = GO(1, 2, 3)
go.print()
p1 = Point(1, 2, 3, 10, 20)
p1.print()

#Common handling 
G = [go, p1]

for g in G:
    g.print()

#Mutable vs Immutable
L1 = [1, 2, 3]
print(id(L1))
L2 = L1
print(id(L2))

#Shallow copy
print(id(p1))
p2 = p1
print(id(p2))
p1.x = 25
p1.print()
p2.print()

#Deep copy
p3 = deepcopy(p1)
print(id(p3))
p1.x=105   
p3.y=-12
p1.print()
p3.print()

#Comparison, operators <, >, ==
print(p1 < p3)
print(p1 > p3)

p4 = deepcopy(p1)
print(p1 == p4)

#Sort a list
L = [5, 4, 9]
L.sort()
print(L)
LS = sorted(L)
print(LS)

#Sort by x, ascendent order
LP = [p1, p2, p3]
LP.sort()
LP[0].print()
LP[2].print()
#LSP = sorted(LP)

#Sort by y, decendent order
LP.sort(key=lambda k: k.y, reverse=True)    #Lambda value
LP.sort(key= attrgetter('y'))               #Attribute getter
LP[0].print() 
LP[2].print()

#Sort by distance from T, own function
T = Point(0,0)
LP.sort(key=lambda k: dist(k, T), reverse=True)