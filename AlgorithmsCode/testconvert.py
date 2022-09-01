plaintext = 'Pound'
plaintext += ' '      # this will get thrown away for even lengths
for i in range(0, len(plaintext), 2):
        group = plaintext[i: i+2]
        plain_number = ord(group[0]) * 256 + ord(group[1])
        encrypted = pow(plain_number, 8, 11377)
print(plain_number)
print(encrypted)
