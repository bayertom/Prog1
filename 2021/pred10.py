#2D point
class Point:
    counter = 0

    def __init__(self, x=0, y=0):
       self.__id = Point.counter 
       self.__x = x
       self.__y = y
       Point.counter = Point.counter + 1
    
    def print(self):
        print(self.__id, self.__x, self.__y)

    @staticmethod
    def getAmountOfObjects():
        return Point.counter


#Create objects, print amount of objects
p1 = Point(10, 15)
print('Objects:', Point.getAmountOfObjects())
p2 = Point(37, 20)
print('Objects:', Point.getAmountOfObjects())
p3 = Point()
print('Objects:', Point.getAmountOfObjects())

#Print properties
p1.print()
p2.print()
p3.print()
p1.__x = 27
p1.__y = 15




