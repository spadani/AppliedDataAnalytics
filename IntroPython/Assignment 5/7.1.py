#7.1 (The Rectangle class)

class Rectangle:

    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return (self.width * 2) + (self.height * 2)


def main():
    rectangle1 = Rectangle(4, 40)
    print("Width", rectangle1.width, "Height:", rectangle1.height,
          "Area:", rectangle1.getArea(), "Perimeter:", rectangle1.getPerimeter())
    rectangle2 = Rectangle(3.5, 35.7)
    print("Width", rectangle2.width, "Height:", rectangle2.height,
          "Area:", format(rectangle2.getArea(), "2f"), "Perimeter:", rectangle2.getPerimeter())


main()

