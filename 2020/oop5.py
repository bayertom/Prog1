class Ellipse:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def print(self):
        print(self._a, self._b)

    def resize(self, a, b):
        self._a = a
        self._b = b

class Circle(Ellipse):
    def __init__(self, r):
        super().__init__(r, r)

    def resize(self, a, b):
        if (a != b):
            b = a
        super().__init__(a, b)

o1 = Ellipse(2, 1)
o1.print()
o1.resize(4, 0.5)
o1.print()
o2 = Circle(5)
o2.print()
o2.resize(0.5, 5)
o2.print()
#L = [o1, o2]
#L[0].resize()