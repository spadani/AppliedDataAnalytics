
def displayPermuationHelper(s1, s2):
    #use loop to move character from s2 to s1 and recursively invoke it with a new s1 and s2. base case is that
    # s2 is empty and prints s1 to the console

    if s2 == "":
        print(s1)
    else:
        for i in range(len(s2)):
            s2_character = s2[i]
            s1_new = s1 + s2_character
            s2_new = s2[:i] + s2[i+1:]
            displayPermuationHelper(s1_new, s2_new)


def displayPermutation(s):
    return displayPermuationHelper("", s)


def main():
    string = input("Please enter a string to display permutations: ")
    displayPermutation(string)


main()


