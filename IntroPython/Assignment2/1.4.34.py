# calculate decimal from hexvalue input



def hex_decimal(hexvalue):
    try:
        dec = int(hexvalue, 16)
        print(dec)
    except ValueError:
        print("Invalid input")


# take in user input and print decimal value from hex character
def main():
    hexvalue = input("Enter a hex character: ")
    hex_decimal(hexvalue)


main()
