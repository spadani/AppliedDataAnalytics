# calculate day of week from any date input


def calculate_day(dom, m, cent, year):
    if m == 1 or m == 2:
        m += 12
        year -= 1
    # algorithm implementation
    day = (dom + ((26 * (m+1)) // 10) + year + (year/4) + (cent/4) + (5*cent)) % 7
    # assign day to number
    if day == 0:
        day = 'Saturday'
    elif day == 1:
        day = 'Sunday'
    elif day == 2:
        day = 'Monday'
    elif day == 3:
        day = 'Tuesday'
    elif day == 4:
        day = 'Wednesday'
    elif day == 5:
        day = 'Thursday'
    elif day == 6:
        day = 'Friday'
    return day


def main():

    # user inputs and call back to calculate_day function
    year = eval(input("Enter year: (e.g., 2008): "))
    cent = year // 100
    year = year % 100
    m = eval(input("Enter month: 1-12: "))
    dom = eval(input("Enter day of the month: 1-31: "))
    day = calculate_day(dom, m, cent, year)
    print("The day of the week is", day)


main()
