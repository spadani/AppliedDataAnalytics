

polynomial = "(x**2 + 5x**2 - 3x + 3) + (4x**5 - 2x**2 + 1)"

variations = []
for i, char in enumerate(polynomial):
    if char == '(':
        start = i
    if char == ')':
        end = i
    print(polynomial[start:end])

    if char == '(':
        subset = polynomial[i+1:]
    if char == '*':
        print(polynomial[i])








variations = []
for i, char in enumerate(polynomial):
    if char == 'x':
        if polynomial[i+1] == '*':
            variations.append(polynomial[i:i+4])
        else:
            variations.append(polynomial[i])
        poly = list(set(variations))
    else:
        continue

print('variations', poly)

for i, char in enumerate(polynomial):
    for j, pattern in enumerate(poly):
        similar = []
        if polynomial[i:i+4] == poly[j]:
            if polynomial[i-1] == '(':
                similar.append(polynomial[i:i+4])
            else:
                similar.append(polynomial[i-3:i+4])
        values = []
        for patternfound in similar:
            for k, found in enumerate(patternfound):
                if found == 'x':
                    values.append(patternfound[k-1])
                else:
                    continue
        test_list = [int(i) for i in values]
        print(sum(test_list))