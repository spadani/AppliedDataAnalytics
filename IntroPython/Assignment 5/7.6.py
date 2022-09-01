import math


class QuadraticEquation:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def geta(self):
        return self.a

    def getb(self):
        return self.b

    def getc(self):
        return self.c

    def getdiscriminant(self):
        discriminant = (self.getb() * self.getb()) - (4 * self.geta() * self.getc())
        return discriminant

    def getroot1(self):
        root1 = (-(self.getb()) + math.sqrt(self.getdiscriminant()))/(2 * self.geta())
        return root1

    def getroot2(self):
        root2 = (-(self.getb()) - math.sqrt(self.getdiscriminant())) / (2 * self.geta())
        return root2


def main():
    a = eval(input("Enter value for a: "))
    b = eval(input("Enter value for b: "))
    c = eval(input("Enter value for c: "))
    quadratic = QuadraticEquation(a, b, c)
    if quadratic.getdiscriminant() < 0:
        print("The equation has no roots")
    elif quadratic.getdiscriminant() == 0:
        print(quadratic.getroot1())
    else:
        print("Root1:", quadratic.getroot1(), "Root2:", quadratic.getroot2())


main()
