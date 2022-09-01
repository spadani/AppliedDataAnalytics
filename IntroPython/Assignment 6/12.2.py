
class Location:

    def __init__(self, row, column, maxValue):
        self.row = row
        self.column = column
        self.maxValue = maxValue

    def getrow(self):
        return self.row

    def getcolumn(self):
        return self.column

    def getmaxvalue(self):
        return self.maxValue


def main():

    row, column = eval(input("Enter the number of rows and columns in the list: "))

    rowcolumn = []
    for i in range(row):
        rowvalues = eval(input("Enter value for row " + str(i) + ": "))
        num = [x for x in rowvalues]
        rowcolumn.append(num)

    location = locatelargest(rowcolumn)
    print("The largest element is located at (" + str(location.getrow()) + " , " + str(location.getcolumn())
          + ") and the largest element is " + str(location.getmaxvalue()))


def locatelargest(a):
    row = 0
    column = 0
    maxValue = a[0][0]
    for k in range(len(a)):
        for j in range(len(a[k])):
            if a[k][j] > maxValue:
                maxValue = a[k][j]
                row = k
                column = j

    return Location(row, column, maxValue)


main()





