shoppinglst= ['milk','chesse','butter']


print(shoppinglst[1])
print(shoppinglst[-3])

print('milk' in shoppinglst)

for i in shoppinglst:
    print(i)

for i in range(len(shoppinglst)):
    shoppinglst[i] = shoppinglst[i]   + "+"
    print(shoppinglst[i])