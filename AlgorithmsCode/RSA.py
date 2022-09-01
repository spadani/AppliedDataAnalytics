import random
import sys
import string

#Public Key Generation
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

n = (p*q)
print("n value")
print(n)

#calculate p(n)
phi = ((p-1)*(q-1))
print("p(n) value")
print(phi)

#generate e
#e = [i for i in range(1,(x-1))]
#print("e value")
#print(e)

#e = random.randint(1,x)
e = 65537
print("e value")
print(e)


def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x

d = modinv(e, phi)
print('This is d', d)

#Private Key Generation
#d = (1 % x) / e
#print("d value")
#d = round(d)
#print(d)

#Private Key Generation
#d = (((2*(x))+1)/e)
#d = round(d)
#print("d value", d)
#print('does this equal 1?', (d*e) % x)


#Send Public Key (basically the public key will exists in a variable the encryption step can use)


#generate random message/word (there exists a pypi function to generate random words, you can figure out how to install it: https://pypi.org/project/Random-Word/)
#from random_word import RandomWords
#r = RandomWords()
#message = r.get_random_word()
#message = message.upper()
#print(message)
message = "IGUANA"

#convert word to number format:encryptedMessageNum
encryptedMessageNum = ""
for letter in message:
    y = ord(letter)
    z = str(y)
    encryptedMessageNum = encryptedMessageNum+z
print ('ENCRYPTED NUMBER', encryptedMessageNum)
encryptedMessageNum = int(encryptedMessageNum)


def encrypt_block(m):
    c = modinv(m**e, n)
    return c


for letter in message:
    EncryptedMessageNumNEW = chr(encrypt_block(ord(letter)))
print('encrypted number new', EncryptedMessageNumNEW)

#cc = modinv(ord(message)**e, n)

#print('this is c', cc)

#def decrypt_block(c):
#    m = modinv(c**d, n)
#    if m == None: print('No modular multiplicative inverse for block ' + str(c) + '.')
#    return m


#cipherText = (messageNum)^e mod n
cipherText = ((encryptedMessageNum ** e) % n)
print("cipherText")
print(cipherText)

#sample modulo example
#issue is that this isn't working for numbers (where 698) larger than 3 digits... but here: http://doctrina.org/How-RSA-Works-With-Examples.html they do this with
#an extremely large numer so why is the inverse operation failing here.

#encryption key = (3,27221)

#decryption key = (17928,27221)

ex1 = ((12345 ** 3)%27221)
ex2 = ((ex1 ** 17928)%27221)
#ex1 = ((698 ** 3)%3127)
#ex2 = ((ex1 ** 2011)%3127)
#print("Example")
#print(ex1)
#print("match", ex2)

#send back message

#Decryption
#decryptedMessageNum^d mod n
decryptedMessageNum = 0
decryptedMessageNum = ((cipherText ** d) % n)
print('DECRYPTED NUMBER', decryptedMessageNum)

#convert decryptedMessageNum to word format

#Display Decrypted Message
#print(r) (word used in original message
#if they match, algorithm worked

#Case structure this with UI


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

inputString = message
numberOutput = int(bit_list_to_string(string_to_bits(inputString)),2) #1976620216402300889624482718775150

bitSeq = seq_to_bits(bin(numberOutput)[2:]) #[2:] is needed to get rid of 0b in front
paddedString = pad_bits(bitSeq,len(bitSeq) + (8 - (len(bitSeq) % 8))) #Need to pad because conversion from dec to bin throws away MSB's
outputString = bits_to_string(paddedString) #attack at dawn
print("")
print("")
print("EXAMPLE STARTS HERE")
print("")
print("")
#print(numberOutput)
#print(outputString)

#ex3 = ((12345 ** 3)%27221)
#print(ex3)
#ex4 = ((ex3 ** 17928.333)%27221)
#print("Example")
#print(ex3)
#print("match", ex4)



