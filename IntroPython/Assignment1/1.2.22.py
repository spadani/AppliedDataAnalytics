# (Population projection) The US Census Bureau projects population
# based on the following assumptions:
# One birth every 7 seconds
# One death every 13 seconds
# One new immigrant every 45 seconds
# Write a program to display the population for each of the next five years.
# Assume the current population is 312032486 and one year has 365 days.
# Hint: in Python, you can use integer division operator // to perform division.
# The result is an integer. For example,5 // 4is1(not1.25)and10 // 4is2(not2.5).
# Rewrite Exercise 1.11 to prompt the user to enter the number of years and displays
# the population after that many years.


def get_pop(years):
    current_pop = 312032486
    seconds_year = 31536000
    births_year = (seconds_year * years) // 7
    deaths_year = (seconds_year * years) // 13
    immigrants_year = (seconds_year * years) // 45
    return current_pop + births_year - deaths_year + immigrants_year


def main():
    years = eval(input("Please enter the number of years: "))
    print("The population after", years, "years is", get_pop(years))


main()
