import math


def get_average(total, times_called):
    return total / times_called


def main():
    total = 0
    times_called = 0
    finished = False
    numbers_list = []
    standard_deviation = 0
    while not finished:
        response = input("Enter number or hit enter to finish: ")
        if response:
            times_called += 1
            number = eval(response)
            total += number
            numbers_list.append(number)
        else:
            finished = True
            if times_called > 0:
                average = get_average(total, times_called)
                for number in numbers_list:
                    variation = (number - average) ** 2
                    standard_deviation += variation
                standard_deviation = math.sqrt(standard_deviation / times_called)
    if times_called > 0:
        print("The average is", get_average(total, times_called))
        print("The standard deviation is", standard_deviation)
    else:
        print("No numbers entered")


main()


