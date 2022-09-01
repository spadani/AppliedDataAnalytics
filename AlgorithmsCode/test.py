
"""
This program implements the RSA algorithm for cryptography.
It randomly selects two prime numbers from a txt file of prime numbers and
uses them to produce the public and private keys. Using the keys, it can
either encrypt or decrypt messages.
"""

import random


def gcd(a, b):
    """
    Performs the Euclidean algorithm and returns the gcd of a and b
    """
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)


def xgcd(a, b):
    """
    Performs the extended Euclidean algorithm
    Returns the gcd, coefficient of a, and coefficient of b
    """
    x, old_x = 0, 1
    y, old_y = 1, 0

    while (b != 0):
        quotient = a // b
        a, b = b, a - quotient * b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    return a, old_x, old_y


#GET PRIME NUMBERS
def isPrime(x):
    if x > 1:
        # Iterate from 2 to n / 2
        for i in range(2, x // 2):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (x % i) == 0:
                return False
        else:
            return True
    else:
        return False


def chooseE(totient):
    """
    Chooses a random number, 1 < e < totient, and checks whether or not it is
    coprime with the totient, that is, gcd(e, totient) = 1
    """
    while (True):
        e = random.randrange(2, totient)

        if (gcd(e, totient) == 1):
            return e

def chooseKeys():
    """
    Selects two random prime numbers from a list of prime numbers which has
    values that go up to 100k. It creates a text file and stores the two
    numbers there where they can be used later. Using the prime numbers,
    it also computes and stores the public and private keys in two separate
    files.
    """

    primes = [i for i in range(500, 1000) if isPrime(i)]

    prime1 = random.choice(primes)
    prime2 = random.choice(primes)

    # compute n, totient, e
    n = prime1 * prime2
    totient = (prime1 - 1) * (prime2 - 1)
    e = 65537

    # compute d, 1 < d < totient such that ed = 1 (mod totient)
    # e and d are inverses (mod totient)
    gcd, x, y = xgcd(e, totient)

    # make sure d is positive
    if (x < 0):
        d = x + totient
    else:
        d = x

    return n, d, e

def encrypt(message, n, d, e, file_name='public_keys.txt', block_size=2):
    """
    Encrypts a message (string) by raising each character's ASCII value to the
    power of e and taking the modulus of n. Returns a string of numbers.
    file_name refers to file where the public key is located. If a file is not
    provided, it assumes that we are encrypting the message using our own
    public keys. Otherwise, it can use someone else's public key, which is
    stored in a different file.
    block_size refers to how many characters make up one group of numbers in
    each index of encrypted_blocks.
    """


    encrypted_blocks = []
    ciphertext = -1

    if (len(message) > 0):
        # initialize ciphertext to the ASCII of the first character of message
        ciphertext = ord(message[0])

    for i in range(1, len(message)):
        # add ciphertext to the list if the max block size is reached
        # reset ciphertext so we can continue adding ASCII codes
        if (i % block_size == 0):
            encrypted_blocks.append(ciphertext)
            ciphertext = 0

        # multiply by 1000 to shift the digits over to the left by 3 places
        # because ASCII codes are a max of 3 digits in decimal

        ciphertext = ciphertext * 1000 + ord(message[i])

    # add the last block to the list
    encrypted_blocks.append(ciphertext)

    # encrypt all of the numbers by taking it to the power of e
    # and modding it by n
    for i in range(len(encrypted_blocks)):
        encrypted_blocks[i] = str((encrypted_blocks[i] ** e) % n)

    # create a string from the numbers
    encrypted_message = " ".join(encrypted_blocks)

    print(encrypted_message)
    return encrypted_message


def decrypt(blocks, n, d, e, block_size=2):
    """
    Decrypts a string of numbers by raising each number to the power of d and
    taking the modulus of n. Returns the message as a string.
    block_size refers to how many characters make up one group of numbers in
    each index of blocks.
    """
    print(n, d)
    # turns the string into a list of ints
    list_blocks = blocks.split(' ')
    int_blocks = []

    for s in list_blocks:
        int_blocks.append(int(s))

    message = ""

    # converts each int in the list to block_size number of characters
    # by default, each int represents two characters
    for i in range(len(int_blocks)):
        # decrypt all of the numbers by taking it to the power of d
        # and modding it by n
        int_blocks[i] = (int_blocks[i] ** d) % n

        tmp = ""
        # take apart each block into its ASCII codes for each character
        # and store it in the message string
        for c in range(block_size):
            tmp = chr(int_blocks[i] % 1000) + tmp
            int_blocks[i] //= 1000
        message += tmp
    print(message)
    return message

# this is e 40031
# this is d 36683
# this is n 76033

#     # we select our primes and generate our public and private keys,
#     # usually done once
#     choose_again = input('Do you want to generate new public and private keys? (y or n) ')
#     if (choose_again == 'y'):
#         chooseKeys()
#
#     instruction = input('Would you like to encrypt or decrypt? (Enter e or d): ')
#     if (instruction == 'e'):
#         message = input('What would you like to encrypt?\n')
#         option = input('Do you want to encrypt using your own public key? (y or n) ')
#
#         if (option == 'y'):
#             print('Encrypting...')
#             print(encrypt(message))
#         else:
#             file_option = input('Enter the file name that stores the public key: ')
#             print('Encrypting...')
#             print(encrypt(message, file_option))
#
#     elif (instruction == 'd'):
#         message = input('What would you like to decrypt?\n')
#         print('Decryption...')
#         print(decrypt(message))
#     else:
#         print('That is not a proper instruction.')

n, d, e = chooseKeys()
blocks = encrypt('ngdhfjkl;', n, d, e)
msg = decrypt(blocks, n, d, e)
