# 2. 13 (Split digits)
# Write a program that prompts the user to enter a four-digit integer and
# displays the number in reverse order

variable = 10


def reverse():
    """ This function takes in a 4 digit integer and prints the integer in reverse order

    """
    num = eval(input("Please enter an integer here: "))
    digit1 = num % variable
    num = num // variable
    digit2 = num % variable
    num = num // variable
    digit3 = num % variable
    num = num // variable
    digit4 = num % variable
    print(digit1)
    print(digit2)
    print(digit3)
    print(digit4)


def main():
    reverse()


main()

