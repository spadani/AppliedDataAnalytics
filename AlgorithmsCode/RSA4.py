import random
import sys
import string

# #GET PRIME NUMBERS
# def isPrime(x):
#     count = 0
#     for i in range(int(x/2)):
#         if x % (i+1) == 0:
#             count = count+1
#         return count == 1
#
# primes = [i for i in range(100,1000) if isPrime(i)]
#
# p = random.choice(primes)
# q = random.choice(primes)
# if q == p:
#     q = random.choices(primes)
#
# print("first prime")
# print(p)
# print("second prime")
# print(q)
#
# ## CREATE PUBLIC KEY
# n = (p*q)
# print("n value")
# print(n)
#
# #calculate p(n)
# x = ((p-1)*(q-1))
# print("p(n) value")
# print(x)
#
# e = 65537
# print("e value")
# print(e)
#
# # CREATE PRIVATE KEY D
# def modinv(a, m):
#     for x in range(1, m):
#         if (a * x) % m == 1:
#             return x
#     return None
#
# print("TESTING D")
# print(modinv(e, x))
# d = modinv(e, x)
# print(d)
# print("return 1", (d*e) % x)

#cipherText = ((encryptedMessageNum ** e) % n)
#print("Cipher Text", cipherText)

#########################


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


def chooseE(totient):
    """
    Chooses a random number, 1 < e < totient, and checks whether or not it is
    coprime with the totient, that is, gcd(e, totient) = 1
    """
    while (True):
        e = random.randrange(2, totient)

        if (gcd(e, totient) == 1):
            return e


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


primes = [i for i in range(2, 1000) if isPrime(i)]

p = random.choice(primes)
q = random.choice(primes)
print(p)
print(q)
if q == p:
    q = random.choices(primes)


# choose two random numbers within the range of lines where
# the prime numbers are not too small and not too big
#rand1 = random.randint(100, 300)
#rand2 = random.randint(100, 300)

# store our prime numbers in these variables
prime1 = p
prime2 = q
print(prime1)

# compute n, totient, e
n = prime1 * prime2
totient = (prime1 - 1) * (prime2 - 1)
e = chooseE(totient)


# compute d, 1 < d < totient such that ed = 1 (mod totient)
# e and d are inverses (mod totient)
gcd, x, y = xgcd(e, totient)

# make sure d is positive
if (x < 0):
    d = x + totient
else:
    d = x

print('this is e', e)
print('this is d', d)
print('this is n', n)
print('this is phi', totient)

message = "cat"
block_size = 2

encrypted_blocks = []
ciphertext = -1

if len(message) > 0:
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
    encrypted_blocks[i] = str((encrypted_blocks[i]**e) % n)

# create a string from the numbers
encrypted_message = " ".join(encrypted_blocks)

print('this is the new encryption', encrypted_message)

#send back message

#DECRYPT MESSAGE

#decryptedMessageNum = ((cipherText ** d) % n)
#print('decrypted number', decryptedMessageNum)

###################


"""
Decrypts a string of numbers by raising each number to the power of d and
taking the modulus of n. Returns the message as a string.
block_size refers to how many characters make up one group of numbers in
each index of blocks.
"""

blocks = encrypted_message

# turns the string into a list of ints
list_blocks = blocks.split(' ')
# print(list_blocks)
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
    # print(int_blocks[i])

    tmp = ""
    # take apart each block into its ASCII codes for each character
    # and store it in the message string
    for c in range(block_size):
        # print(int_blocks)
        # print(int_blocks[i] % 1000)
        tmp = chr(int_blocks[i] % 1000) + tmp
        int_blocks[i] //= 1000
    message += tmp
print('decrypted message', message)