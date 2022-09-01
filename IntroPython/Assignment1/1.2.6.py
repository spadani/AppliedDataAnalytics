# 2.6 (Sum the digits in an integer)
# Write a program that reads an integer between 0 and 1000 and adds all the digits in the integer.
# For example, if an integer is 932, the sum of all its digits is 14. (Hint: Use the % operator to extract digits,
# and use the // operator to remove the extracted digit. For instance, 932 % 10 = 2 and 932 // 10 = 93.)


def integer():
    variable = 10

    num = eval(input("Please enter an integer here: "))
    digit1 = num % variable
    num = num // variable
    digit2 = num % variable
    num = num // variable
    digit3 = num % variable
    num = num // variable
    digit4 = num % variable
    print(digit1 + digit2 + digit3 + digit4)


def main():
    integer()


main()

