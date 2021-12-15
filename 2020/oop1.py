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


#Vytvoreni objektu
p1 = Point()
p1.print()

p2 = Point(3, 4)
p2.print()

p3 = Point(-5, 7)
p3.print()

#Volani metody
p1.print()
p2.print()
p3.print()

#Pocet objektu, staticka funkce
obj = Point.amountOfObjects()
print(obj)

#Zmena hodnoty, spatne, nepouzito zapouzdreni
print(p1.getX())
p1.setX(45)
print(p1.getX())

p1.x = 10
print(p1.x)
#p1.y = 10
#p1.print()