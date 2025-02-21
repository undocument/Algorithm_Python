my_list= [10,20,30,40,50,60,70,80,90]


# in operation
target = 50

if target in my_list:
    print("target is there")

else:
    print("target is not there")


#linear seacrh

def linearSearch(list, target):
    for i, value in enumerate(list):
        if value== target:
            return i
    return -1

print(linearSearch(my_list, target))