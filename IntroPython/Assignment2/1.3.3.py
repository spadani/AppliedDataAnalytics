# Atlanta, Georgia: 33.753746, -84.386330 (LAT, LONG)
# Orlando, FL: 28.538336, -81.379234 (LAT, LONG)
# Savannah, Georgia: 32.076176, -81.088371 (LAT, LONG)
# Charlotte: 35.227085, -80.843124 (LAT, LONG)

# take in longitude coordinates and return the total area


import math as m


def triangle(x1, x2, x3, x4, y1, y2, y3, y4):
    # define the sides of the two triangles
    # side 1 represents the same side on both triangles
    # take value 6371.01 = km of radius and return the number in radians
    t1side1 = m.radians(6371.01) * m.acos(m.sin(x1) * m.sin(x2) + m.cos(x1) * m.cos(x2) * m.cos(y1 - y2))
    t1side2 = m.radians(6371.01) * m.acos(m.sin(x3) * m.sin(x2) + m.cos(x3) * m.cos(x2) * m.cos(y3 - y2))
    side = m.radians(6371.01) * m.acos(m.sin(x1) * m.sin(x3) + m.cos(x1) * m.cos(x3) * m.cos(y1 - y3))
    t2side1 = m.radians(6371.01) * m.acos(m.sin(x1) * m.sin(x4) + m.cos(x1) * m.cos(x4) * m.cos(y1 - y4))
    t2side2 = m.radians(6371.01) * m.acos(m.sin(x3) * m.sin(x4) + m.cos(x3) * m.cos(x4) * m.cos(y3 - y4))
    # triangle 1 area
    s1 = (t1side1 + t1side2 + side)/2
    a1 = m.sqrt(s1 * (s1 - t1side1) * (s1 - t1side2) * (s1 - side))
    # triangle 2 area
    s2 = (t2side1 + t2side2 + side) / 2
    a2 = m.sqrt(s2 * (s2 - t2side1) * (s2 - t2side2) * (s2 - side))
    # print total area
    print(a1+a2)


def main():
    # takes in coordinates of the 4 cities and returns the total area
    return triangle(33.753746, -84.386330, 28.538336, -81.379234, 32.076176, -81.088371, 35.227085, -80.843124)


main()

