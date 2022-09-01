
"""
Implementation of the RSA algorithm using encryption and decryption for a message The program initializes 2 prime numbers,
a phi value denoted here as x, a d value, and a standard e value = 65537.
"""

import random


RANDOM_PRIME_START = 500
RANDOM_PRIME_STOP = 1000
ASCII_CONSTANT = 1000
SIZE = 2


def getrandomprimes():
    primes = []
    for possibleprime in range(RANDOM_PRIME_START, RANDOM_PRIME_STOP):
        not_prime = False
        for i in range(2, possibleprime // 2):
            if (possibleprime % i) == 0:
                not_prime = True
                break
        if not not_prime:
            primes.append(possibleprime)

    return random.choice(primes), random.choice(primes)


#def inverse(a, m):
#    for x in range(1, m):
 #       if (a * x) % m == 1:
 #           return x
 #   return None


# Choose 2 random prime numbers denoted as p and q
p, q = getrandomprimes()

# Calculate N
n = (p*q)

# Calculate X (phi value also known as the totient in the RSA algorithm
x = (p - 1) * (q - 1)

# Set the standard e value
e = 65537

d = int(((2*(x))+1)/e)



# Encrypt the message
def encrypt_message(message, n, e):
    encryptednums = []
    # start ciphertext with first char
    ciphertext = ord(message[0])

    for i in range(1, len(message)):
        # reset the ciphertext every time we reach the SIZE
        if i % SIZE == 0:
            encryptednums.append(ciphertext)
            # reset the cipher text to 0
            ciphertext = 0

        ciphertext = ciphertext * ASCII_CONSTANT + ord(message[i])

    # add the last block to the list
    encryptednums.append(ciphertext)

    # encrypt all of the numbers by taking it to the power of e
    # and modding it by n
    for i in range(len(encryptednums)):
        encryptednums[i] = str((encryptednums[i] ** e) % n)

    # convert to a string
    encrypted_message = " ".join(encryptednums)

    return encrypted_message

# Decrypt

# Takes the string and converts it to the decrypted number using the decrypted block function and then returns the final message
def decrypt_message(encrypted_message, n, d):
    message = ""

    encrypted_list = encrypted_message.split(' ')

    for i in range(len(encrypted_list)):
        encrypted_ints = int(encrypted_list[i])

        message += decrypt_block(encrypted_ints, n, d)

    return message

#Helper function to decrypt the numbers and return the final message
def decrypt_block(encrypted_ints, n, d):
    chars = ''

    # decrypt all of the numbers by taking it to the power of d and modding by n
    decrypted_ints = (encrypted_ints ** d) % n
    print('Decrypted Number', decrypted_ints)

    # take apart each block into its ASCII codes for each character
    # and store it in the message string
    # converts each int in the list to block_size number of characters
    # by default, each int represents two characters
    for c in range(SIZE):
        chars = chr(decrypted_ints % ASCII_CONSTANT) + chars
        decrypted_ints //= ASCII_CONSTANT

    return chars


# USER INPUT: INPUT MESSAGE
inputmessage = input('Enter Message Here: ')

# ENCRYPT THE MESSAGE
encrypted_input = encrypt_message(inputmessage, n, e)
print('Encrypted Number', encrypted_input)

# DECRYPT THE MESSAGE
msg = decrypt_message(encrypted_input, n, d)
print('FINAL MESSAGE:', msg)

