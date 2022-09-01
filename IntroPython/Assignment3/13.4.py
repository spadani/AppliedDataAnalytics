import random
import os

# Write a program that writes 100 integers created randomly into a file.
# Integers are separated by a space in the file. Read the data back from the
# file and display the sorted data. Your program should prompt the user to enter a filename.
# If the file already exists, do not override it. Here is a sample run:
# (Page 492).


def main():
    filename = input("Enter a file name: ")
    if os.path.isfile(filename):
        print(filename, "exists")
    else:
        num_list = []
        for i in range(100):
            outfile = open(filename, "w")
            numbers = str(random.randint(0, 100))
            num_list.append(numbers)
        outfile.write(" ".join(num_list))
        outfile.close()

        infile = open(filename, "r")
        s = infile.read()
        numbers = [eval(x) for x in s.split()]
        for number in numbers:
            print(number, end=" ")
        infile.close()


main()




