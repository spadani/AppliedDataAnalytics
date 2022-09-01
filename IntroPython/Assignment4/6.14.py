

m = [1, 101, 201, 301, 401, 501, 601, 701, 801, 901]

print("{:<3s}".format("i"), "{:>2s}".format("m(i)"), end=' ')
print('')
print('')
for number in m:
    pi = 0
    for i in range(0, number):
        pi += ((4.0 * (-1) ** i) / (2 * i + 1))
    print("{:<3d}".format(number), format(pi, '.4f'))
