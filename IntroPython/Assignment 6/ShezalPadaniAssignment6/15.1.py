

def sumDigits(n):
    numlist = [int(d) for d in str(n)]
    newnum = 0
    for number in numlist:
        newnum += number
    print(newnum)


def main():
    number = eval(input("Please enter a number: "))
    sumDigits(number)


main()

