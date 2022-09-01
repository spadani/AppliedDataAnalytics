


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


print(modinv(108**151, 22499))

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

modinv(e,x)



