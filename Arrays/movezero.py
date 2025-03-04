arr = [2,0,4,5,6,0]

def movezero(a):
    last_noonzero_index = 0

    for i in range(len(a)):
        if a[i] !=0:
            a[last_noonzero_index], a[i] = a[i], a[last_noonzero_index]
            last_noonzero_index += 1
    return a

print(movezero(arr))