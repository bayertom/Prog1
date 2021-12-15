from copy import deepcopy
from math import fabs, sqrt
from operator import itemgetter, attrgetter

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

    def __lt__(self, other):
        return self.__x < other.__x

    def __eq__(self, other):
        #return (self.__x == other.__x) and (self.__y == other.__y)
        return (fabs(self.__x - other.__x) < 0.001) and (fabs(self.__y - other.__y) < 0.001)

    def __gt__(self, other):
        return self.__x > other.__x

    def __repr__(self):
        return str(self.__x) + " " + str(self.__y)

def dist(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return sqrt(dx * dx + dy * dy)

p1 = Point(1, 2, 3, 0, 0)
p1.x = 5

p1.print()

#Melka kopie
p2 = p1
p2.print()
p3 = p2
p3.print()

#Hluboka kopie
p4 = deepcopy(p1)
p4.print()
p1.x = 20
p1.print()
print(p3<p4)
print(p1==p2)

#Trideni, operator lt
p5 = Point(1, 2, 3, 10, 10)
p6 = Point(1, 2, 3, -5, 7)
p7 = Point(1, 2, 3, -2, -10)
p8 = Point(1, 2, 3, 1, 1)
L = [p1, p2, p3, p4, p5, p6, p7, p8]
print(L)
L.sort(reverse=True)
print(L)

#Trideni, lambda
L.sort(key = lambda k: k.y)
print(L)

#Trideni, attrgetter
LS = sorted(L, key = attrgetter('x'))
print(LS)

#Trideni, komparacni funkce
q = Point(2, 2)
L.sort(key = lambda k: dist(k, q), reverse=True)
print(L)