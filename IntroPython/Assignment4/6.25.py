#(Emirp) An emirp (prime spelled backward) is a nonpalindromic prime number whose reversal is also a prime.
# For example, both 17 and 71 are prime numbers, so 17 and 71 are emirps.
# Write a program that displays the first 100 emirps.
#Display 10 numbers per line and align the numbers properly, as follows: 13 17 31 37 71 73 79 97 107 113 149 157 167 179 199 311 337 347 359 389


def prime(number):
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def main():
    primecount = 0
    currentnumber = 0
    while primecount < 100:
        currentnumber += 1
        if prime(currentnumber):
            getreverse = list(str(currentnumber))
            getreverse.reverse()
            getreverse = ''.join(getreverse)
            getreverse = int(getreverse)
            if prime(getreverse) and getreverse != currentnumber:
                primecount += 1
                print("{:<5d}".format(currentnumber), '', end='')
                if primecount % 10 == 0:
                    print(end='\n')


main()
