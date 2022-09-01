import string

alphabet = string.ascii_lowercase


def main():
    infile = open("charlesdickens.txt", "r")
    character_list = infile.read()
    letter_counts = []
    total_count = 0

    for letter in alphabet:
        letter_counts.append(0)

    for character in character_list:
        if character.lower() in alphabet:
            index = alphabet.index(character.lower())
            letter_counts[index] += 1
            total_count += 1
    outfile = open("counts_dickens.csv", "w")
    outfile.write("Char,Freq,%total" + "\n")
    for letter in alphabet:
        index = alphabet.index(letter)
        percentage = (letter_counts[index] / total_count) * 100
        print_list = [letter, str(letter_counts[index]), str(round(percentage, 2))]
        outfile.write(",".join(print_list) + "\n")
    outfile.close()


main()







