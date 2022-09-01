
def gcd(m, n):
    if m % n == 0:
        return n
    else:
        return gcd(n, m % n)


def main():
    userinput = eval(input("Please enter two integers: "))
    numlist = [x for x in userinput]
    print(gcd(numlist[0], numlist[1]))


main()


