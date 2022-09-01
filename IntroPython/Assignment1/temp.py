# Programming Exercises (Page 56 - 61)

# 2.6, 2.7, 2.13, 2.14, 2.21, 2.22

# (Convert Celsius to Fahrenheit) Write a program that reads a Celsius
# degree from the console and converts it to Fahrenheit and displays
# the result. The formula for the conversion is as follows:
# fahrenheit = (9 / 5) * celsius + 32


def c2f(celsius):
    """ This function converts celsius to fahrenheit

    :param celsius: (int)
    :return: int
    """
    return 9/5 * celsius + 32


def main():
    temp = eval(input("Please enter the temperature in Celsius: "))
    print("The temperature is", c2f(temp), "degrees Fahrenheit.")


main()
