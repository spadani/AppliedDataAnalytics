import random
import sys
import string

#GET PRIME NUMBERS
def isPrime(x):
    count = 0
    for i in range(int(x/2)):
        if x % (i+1) == 0:
            count = count+1
        return count == 1

primes = [i for i in range(100,1000) if isPrime(i)]
p = random.choice(primes)
q = random.choice(primes)
if q == p:
    q = random.choices(primes)

print("first prime")
print(p)
print("second prime")
print(q)

## CREATE PUBLIC KEY

n = (p*q)
print("n value")
print(n)

#calculate p(n)
x = ((p-1)*(q-1))
print("p(n) value")
print(x)

#generate e
#e = [i for i in range(1,(x-1))]
#print("e value")
#print(e)

#e = random.randint(1,x)
e = 65537
print("e value")
print(e)

# CREATE PRIVATE KEY D

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

print("TESTING D")
print(modinv(e, x))
d = modinv(e, x)
print(d)
print("return 1", (d*e) % x)

#Private Key Generation
#d = (((2*(x))+1)/e)
#d = round(d)
#print("d value", d)
#(d*e) % x = 1

#print('test is', test1)
#d*e mod x = 1


#generate random message/word (there exists a pypi function to generate random words, you can figure out how to install it: https://pypi.org/project/Random-Word/)
#from random_word import RandomWords
#r = RandomWords()
#message = r.get_random_word()
#message = message.upper()
#print(message)

#convert word to number format:encryptedMessageNum
#encryptedMessageNum = ""
#for letter in message:
#    y = ord(letter)
#    z = str(y)
#    encryptedMessageNum = encryptedMessageNum+z
#print ('Encrypted number', encryptedMessageNum)
#encryptedMessageNum = int(encryptedMessageNum)

#cipherText = ((encryptedMessageNum ** e) % n)
#print("Cipher Text", cipherText)


message = "IGUANA"
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

#sample modulo example
#issue is that this isn't working for numbers (where 698) larger than 3 digits... but here: http://doctrina.org/How-RSA-Works-With-Examples.html they do this with
#an extremely large numer so why is the inverse operation failing here.
#ex1 = ((698 ** 3)%3127)
#ex2 = ((ex1 ** 2011)%3127)
#print("Example")
#print(ex1)
#print("match", ex2)

#send back message

#DECRYPT MESSAGE

decryptedMessageNum = ((cipherText ** d) % n)
print('decrypted number', decryptedMessageNum)

def decrypt(blocks, block_size=2):

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

    return message


#convert decryptedMessageNum to word format


#TEST CASE on new convert text to decimal function
BITS = ('0', '1')
ASCII_BITS = 8


def bit_list_to_string(b):
    """converts list of {0, 1}* to string"""
    return ''.join([BITS[e] for e in b])

def seq_to_bits(seq):
    return [0 if b == '0' else 1 for b in seq]

def pad_bits(bits, pad):
    """pads seq with leading 0s up to length pad"""
    assert len(bits) <= pad
    return [0] * (pad - len(bits)) + bits

def convert_to_bits(n):
    """converts an integer `n` to bit array"""
    result = []
    if n == 0:
        return [0]
    while n > 0:
        result = [(n % 2)] + result
        n = n // 2
    return result

def string_to_bits(s):
    def chr_to_bit(c):
        return pad_bits(convert_to_bits(ord(c)), ASCII_BITS)
    return [b for group in
            map(chr_to_bit, s)
            for b in group]

def bits_to_char(b):
    assert len(b) == ASCII_BITS
    value = 0
    for e in b:
        value = (value * 2) + e
    return chr(value)

def list_to_string(p):
    return ''.join(p)

def bits_to_string(b):
    return ''.join([bits_to_char(b[i:i + ASCII_BITS])
        for i in range(0, len(b), ASCII_BITS)])


step1 = convert_to_bits(decryptedMessageNum)
print(step1)
step2 = bit_list_to_string(step1)
print(step2)

inputString = message
numberOutput = int(bit_list_to_string(step1),2) #1976620216402300889624482718775150

bitSeq = seq_to_bits(bin(numberOutput)[2:]) #[2:] is needed to get rid of 0b in front
paddedString = pad_bits(bitSeq,len(bitSeq) + (8 - (len(bitSeq) % 8))) #Need to pad because conversion from dec to bin throws away MSB's
outputString = bits_to_string(paddedString) #attack at dawn

print('final output', numberOutput)
print('string output', outputString)

