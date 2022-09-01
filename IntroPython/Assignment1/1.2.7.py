# 2.7 (Find the number of years and days)
# Write a program that prompts the user to enter the minutes (e.g., 1 billion)
# and displays the number of years and days for the minutes. For simplicity,
# assume a year has 365 days. Here is a sample run:

mins_day = 60 * 24
mins_year = mins_day * 365


def s2y(minutes):
    """ This function converts minutes to years

    :param minutes: (int)
    :return: int
    """
    return minutes // mins_year


def s2d(minutes):
    """ This function converts remainder of years to days

    :param minutes: (int)
    :return: int
    """
    return (minutes % mins_year) / mins_day


def main():
    minutes = eval(input("Enter the number of minutes: "))

    print(minutes, " minutes is approximately", s2y(minutes), "years and", s2d(minutes), "days.")


main()

