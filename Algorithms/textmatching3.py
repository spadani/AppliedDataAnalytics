

polynomial = "(x**2 + 5x**2 - 3x + 3) + (4x**5 - 2x**2 + 1) - ( -1x**2)"

variations = []
indexes = []
for i, char in enumerate(polynomial):
    if char == '(' or char == ')':
        indexes.append(i)
    if char == '+' and polynomial[i+2] == '(' and polynomial[i-2] == ')':
        print('addition')
    if char == '-' and polynomial[i+2] == '(' and polynomial[i-2] == ')':
        print('subtraction')
poly1 = polynomial[indexes[0]+1:indexes[1]]
poly2 = polynomial[indexes[2]+1:indexes[3]]

print(poly1)

answer = []
values = []
values2 = []
#values3 = []
for i, char in enumerate(poly1):
    if char == '*' and poly1[i+1] == '*':
        if poly1[i+2] == '2':
            if i == 1:
                if poly1[i-1] == 'x':
                    values.append(1)
            else:
                values.append(int(poly1[i-2]))
    if char == 'x' and poly1[i+1] != '*':
        values2.append(poly1[i-3:i+2])
    #if char.isdigit() and poly1[i+1] != 'x':
        #values3.append(poly1[i])
print(values)
print(values2)
#print(values3)
