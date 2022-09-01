#Write a program that prompts the user to enter a text file,
# #reads words from the file, and displays all the nonduplicate words in ascending order.


def main():

    filename = input("Enter a filename: ").strip()
    infile = open(filename, "r")

    text = infile.read().split()

    wordcount = {}
    for word in text:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    for key, value in wordcount.items():
        if value < 2:
            print(key)


main()


