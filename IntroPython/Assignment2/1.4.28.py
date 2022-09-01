# check if rectangle 1 overlaps, does not overlap, or is inside rectangle 2


def overlap(center1_x, center1_y, width1, height1,
            center2_x, center2_y, width2, height2):
    # calculate right, left, top, and bottom values
    xcoord2_right = center2_x + width2/2
    xcoord2_left = center2_x - width2/2
    ycoord2_top = center2_y + height2 / 2
    ycoord2_bottom = center2_y - height2 / 2
    xcoord1_left = center1_x - width1/2
    xcoord1_right = center1_x + width1/2
    ycoord1_top = center1_y + height1/2
    ycoord1_bottom = center1_y - height1/2

# evaluate overlap
    if ycoord1_top < ycoord2_bottom or ycoord1_bottom > ycoord2_top:
        print('r2 does not overlap r1')
    elif xcoord1_right < xcoord2_left or xcoord1_left > xcoord2_right:
        print('r2 does not overlap r1')
# check if rectangle is inside
    elif ycoord1_top >= ycoord2_top and xcoord1_right >= xcoord2_right and xcoord1_left <= xcoord2_left and ycoord1_bottom <= ycoord2_bottom:
        print('r2 is inside r1')
# else rectangle 2 overlaps rectangle 1
    else:
        print('r2 overlaps r1')


def main():
    center1_x, center1_y, width1, height1 = eval(input("Enter r1's center x-, y-coordinates, width, and height: "))
    center2_x, center2_y, width2, height2 = eval(input("Enter r2's center x-, y-coordinates, width, and height: "))
    return overlap(center1_x, center1_y, width1, height1, center2_x, center2_y, width2, height2)


main()



