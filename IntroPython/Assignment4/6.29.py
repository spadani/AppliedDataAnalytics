

# convert number to list of numbers
def convertnumber(number):
    numberlist = []
    numstring = str(number)
    numlist = list(numstring)
    for character in numlist:
        numberlist.append(int(character))
    return numberlist


# Return this number if it is a single digit, otherwise, return the sum of the two digits
def getdigit(number):
    sum = 0
    # is a single digit
    if prefixmatched(number, number):
        return number
    else:
        numlist = convertnumber(number)
        for digit in numlist:
            sum += digit
        return sum

# Get the result from Step 2
# Double every second digit from right to left.
# If doubling of a digit results in a two-digit number, add up the two digits to get a single-digit number.
# Now add all single-digit numbers from Step 1.

def sumdoubleevenplace(number):
    digitlist = []
    numlist = convertnumber(number)
    numlist.reverse()
    sum = 0
    for i in range(len(numlist)):
        digit = numlist[i]
        if i % 2 != 0:
            doubledigit = digit * 2
            digitlist.append(getdigit(doubledigit))
    for digit in digitlist:
        sum += digit
    return sum


# Return sum of odd place digits in number from right to left
def sumofoddplace(number):
    sum = 0
    digitlist = convertnumber(number)
    digitlist.reverse()
    for i in range(len(digitlist)):
        digit = digitlist[i]
        # index starts at 0, so check mod 2
        if i % 2 == 0:
            sum += digit
    return sum


# Return true if the digit d is a prefix for number
def prefixmatched(number, d):
    return d == getprefix(number, 1)


# Return the number of digits in d
def getsize(d):
    return len(str(d))


# Return the first k number of digits from number. If the # number of digits in number is less than k, return number.
def getprefix(number, k):
    if getsize(number) < k:
        return number
    # convert number to string
    numstring = str(number)
    # convert string to list
    numlist = list(numstring)
    # get the k digits
    kdigitslist = numlist[0:k]
    # convert to string
    kdigitsstring = ''.join(kdigitslist)
    # convert to integer
    kdigits = int(kdigitsstring)
    return kdigits


# Return true if the card number is valid
def isValid(number):

    totalsum = sumofoddplace(number) + sumdoubleevenplace(number)
    if totalsum % 10 == 0:
        return True
    else:
        return False


def main():
    number = eval(input("Enter credit card number: "))
    if isValid(number):
        print("This credit card is valid")
    else:
        print("This credit card is not valid")


main()
