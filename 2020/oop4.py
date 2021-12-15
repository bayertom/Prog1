from abc import ABC, abstractmethod

class AGO(ABC):
    def __init__(self, color = 0, level = 0, width = 0):
        self._color = color
        self._level = level
        self._width = width

    @abstractmethod
    def print(self):
        pass

#Odvozeni od AGO
class Point(AGO):
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

    def print(self):
        print("\nPoint, attributes + geometry:")
        print(str(self._color), str(self._level), str(self._width))
        print(str(self.__id), str(self.__x), str(self.__y))

#Princip kompozice, odvozeni od GO
class Line (AGO):
    def __init__(self, color, level, width, p1, p2):
        # Inicializator GO
        super().__init__(color, level, width)

        self._p1 = p1
        self._p2 = p2

    def print(self):
        print("\nLine, attributes + geometry:")
        print(str(self._color), str(self._level), str(self._width))
        print("Start:")
        self._p1.print()
        print("End:")
        self._p2.print()

#Vytvoreni AGO
#go1 = AGO(1, 2, 3)
#go1.print()
#go2 = GO(4, 5, 17)
#go2.print()

#Vytvoreni Point, potomek GO
p1 = Point(1, 2, 3, 0, 0)
p1.print()
p2 = Point(1, 2, 3, 10, 10)
p2.print()

#Vytvoreni Line, potomek GO
l = Line(1, 2, 3, p1, p2)
l.print()
