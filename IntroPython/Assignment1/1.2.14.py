# 2.14 (Geometry: area of a triangle)
# Write a program that prompts the user to enter the three points
# (x1, y1), (x2, y2), and (x3, y3) of a triangle and displays its area.


import math


def area(x1, y1, x2, y2, x3, y3):
    """ This function calculates the area of 3 points of a triangle

    :param x1: float, x1 coordinate of the triangle
    :param y1: float, y1 coordinate of the triangle
    :param x2: float, x2 coordinate of the triangle
    :param y2: float, y2 coordinate of the triangle
    :param x3: float, x3 coordinate of the triangle
    :param y3: float, y3 coordinate of the triangle
    :return: area of the triangle
    """
    side1 = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    side2 = math.sqrt(math.pow(x3 - x2, 2) + math.pow(y3 - y2, 2))
    side3 = math.sqrt(math.pow(x3 - x1, 2) + math.pow(y3 - y1, 2))
    s = (side1+side2+side3)/2
    return math.sqrt(s*(s-side1)*(s - side2)*(s-side3))


def main():
    x1, y1, x2, y2, x3, y3 = eval(input("Please enter the 3 points of the triangle: "))
    print("The area of the triangle is", area(x1, y1, x2, y2, x3, y3))


main()







