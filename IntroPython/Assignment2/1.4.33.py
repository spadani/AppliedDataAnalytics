# get the hex value from a decimal value


def get_hex(number):
    hex_value = hex(round(number))
    return hex_value[-1]


# print the hex value if less than 15 else print invalid input

def main():
    number = eval(input("Enter an integer value (0-15): "))
    if 0 <= number <= 15:
        print("The hex number is", get_hex(number))
    else:
        print("Invalid Input")


main()
