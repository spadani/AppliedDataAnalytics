# 2.21 (Financial application: compound value)
# Suppose you save $100 each month into a savings account
# with an annual interest rate of 5%. Therefore, the monthly interest rate is 0.05/12 = 0.00417.
# Write a program that prompts the user to enter a monthly saving amount and displays the
# account value after the sixth month.


def get_interest():
    s = 100
    i = (1 + .05 / 12)
    interest = s * i
    for month in range(5):
        interest = (s + interest) * i
    return interest


def main():
    eval(input("Enter the monthly savings amount: "))
    result = get_interest()
    print("After the sixth month, the account value is", result)


main()
