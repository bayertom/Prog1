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

    #Getter ID
    def getID(self):
        return self.__id

    #Getter x
    def getX(self):
        return self.__x
    
    #Getter y
    def getY(self):
        return self.__y

    #Setter x
    def setX(self, x):
        self.__x = x

    #Setter y
    def setY(self, y):
        self.__y = y

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

class Algorithms:

    def mid1(self, p1, p2):
        xmid = 0.5*(p1.x + p2.x)
        ymid = 0.5*(p1.y + p2.y) 
        return xmid, ymid
    
    def mid2(self, p1, p2):
        xmid = 0.5*(p1.x + p2.x)
        ymid = 0.5*(p1.y + p2.y) 
        return Point(xmid, ymid)

    def mid3(self, p1, p2, pmid):
        pmid.x = 0.5*(p1.x + p2.x)
        pmid.y = 0.5*(p1.y + p2.y) 
    
    def mid4(self, l):
        p1 = l.p1
        p2 = l.p2
        xmid = 0.5*(p1.x + p2.x)
        ymid = 0.5*(p1.y + p2.y) 
        return Point(xmid, ymid)

class Line:
    def __init__(self, p1, p2):
        self.__p1 = p1
        self.__p2 = p2
    
    def print(self):
        print('Line:')
        self.__p1.print()
        self.__p2.print()
    
    @property
    def p1(self):
        return self.__p1

    @property
    def p2(self):
        return self.__p2


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

#Working with getters
id1 = p1.getID()
x1 = p1.getX()
y1 = p1.getY()

print(id1, x1, y1)

#Working with setters
p1.setX(13)
p1.setY(26)
p1.print()

#Using properties
print(p1.x, p1.y)
p1.x = 278
p1.y = 105
p1.print()

#Passing/returning objects, v1
a = Algorithms()
xmid, ymid = a.mid1(p1, p2)
print(xmid, ymid)

#Passing/returning objects, v2
pmid = a.mid2(p1, p2)
pmid.print()

#Passing/returning objects, v3
pmid2 = Point()
a.mid3(p1, p2, pmid2)
pmid2.print()

#Composition
p4 = Point(0,0)
p5 = Point(10,10)
l = Line(p4, p5)
l.print()

#Midpoint
pmid3 = a.mid4(l)
pmid3.print()

