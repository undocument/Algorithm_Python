arr = [12, 35, 1, 10, 34, 1,100]
arr1 = sorted(arr)
print(arr1)
print(arr1[-2])


def secondlargest(a):
    n = len(a)
    largest = 0
    seclargest = 0
    for i in range(n):
        if a[i] > largest:
            largest = a[i]

    for i in range(n):
        if a[i] > seclargest and a[i] != largest:
            seclargest = a[i]
    return seclargest



print(secondlargest(arr))