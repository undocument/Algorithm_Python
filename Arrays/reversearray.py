
a = [1,2,3,5]

def reverseArray(arr):
    # Write your code here
    li =[]
    for i in a[::-1]:
        li.append(i)
    return li

print(reverseArray(a))