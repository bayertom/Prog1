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