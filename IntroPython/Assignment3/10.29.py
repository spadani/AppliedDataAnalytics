# Write a hangman game that randomly generates a word and prompts the user to guess one letter at a time,
# as shown in the sample run. Each letter in the word is displayed as an asterisk. When the user makes a correct
# guess, the actual letter is then displayed. When the user finishes a word, display the number of misses and ask
# the user whether to continue playing. Create a list to store the words, as follows:
import random


words = ["apple", "banana", "mango", "orange", "pineapple", "kiwi", "papaya", "grapes"]


def is_finished(word, guesses):
    current = ""
    for character in word:
        if character in guesses:
            current = current + character
        else:
            current = current + "*"
    return current


def main():
    guesses = []
    word = random.choice(words)
    # while the word still has astericks
    while "*" in is_finished(word, guesses):
        guess = input("Enter a letter in word " + is_finished(word, guesses) + ": ")
        if guess in guesses and guess in word:
            print(guess + " is already in the word")
        elif guess not in word:
            print(guess + " is not in the word")
            guesses.append(guess)
        else:
            guesses.append(guess)

    print("The word is " + word + ". You missed " + str(len(guesses) - len(set(word))) + " times.")


main()


