
def update(pricelist, discount, member):
    if member:
        print(discount)
        discount += 10
        print(id(discount))
    print(discount)
    for i in range(len(pricelist)):
        pricelist[i] *= 1 - (discount/100)


pricelist = [100, 400, 1000]


discount = 10
update(pricelist, discount, True)

print(discount, pricelist)
print(id(discount))
