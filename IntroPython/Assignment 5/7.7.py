
class LinearEquation:

    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def geta(self):
        return self.a

    def getb(self):
        return self.b

    def getc(self):
        return self.c

    def getd(self):
        return self.d

    def gete(self):
        return self.e

    def getf(self):
        return self.a

    def issolvable(self):
        num = (self.geta() * self.getd()) - (self.getb() * self.getc())
        if num != 0:
            return True

    def getx(self):
        x = ((self.gete() * self.getd()) - (self.getb() * self.getf())) / (
                (self.geta() * self.getd()) - (self.getb() * self.getc()))
        return x

    def gety(self):
        y = ((self.geta() * self.getf()) - (self.gete() * self.getc())) / (
                (self.geta() * self.getd()) - (self.getb() * self.getc()))
        return y


def main():
        a = eval(input("Enter value for a: "))
        b = eval(input("Enter value for b: "))
        c = eval(input("Enter value for c: "))
        d = eval(input("Enter value for d: "))
        e = eval(input("Enter value for e: "))
        f = eval(input("Enter value for f: "))
        result = LinearEquation(a, b, c, d, e, f)
        if result.issolvable():
            print("X:", result.getx(), "Y:", result.gety())
        else:
            print("The equation has no solution")


main()
