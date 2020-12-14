class Point:
    #Datova polozka tridy
    counter = 0

    #Inicializator
    def __init__ (self, x = 0, y = 0):
        #Datove polozky objektu
        self.__id = Point.counter
        self.__x = x
        self.__y = y

        #Inkrementace datove polozky tridy
        Point.counter = Point.counter + 1

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    #Getter
    def getX(self):
        return self.__x

    #Setter
    def setX(self, x):
        self.__x = x

    def print(self):
        print(str(self.__id), str(self.__x), str(self.__y))

    @staticmethod
    def amountOfObjects():
        return Point.counter

#Princip kompozice I
class Line:
    def __init__(self, p1, p2):
        self.__p1 = p1
        self.__p2 = p2

    def print(self):
        self.__p1.print()
        self.__p2.print()

#Princip kompozice II
class Polygon:
    def __init__(self, *p):
        self.__vertices = p

    def print(self):
        for p in self.__vertices:
            p.print()

p1 = Point(0, 0)
p2 = Point(10, 0)
p3 = Point(10, 10)
p4 = Point(0, 10)

#Princip kompozice, linie
l = Line(p1, p2)
l.print()

#Princip kompozice, polygon
pol = Polygon(p1, p2, p3, p4)
pol.print()