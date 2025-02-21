from array import *

arr = array('i', [1,2,34,4,5,6,7,8,9])

#1. Create array and traverse

def traverse_Array(array):
    for i in array:
        print(i)
        
        
traverse_Array(arr)


#2 access individual elements through indexes
print("Step 2")
print(arr[4])

#3 append any value to array using append()

print("Step 3")
arr.append(500)
print(arr)

#4 insert value method useing insert()

print("Step 4")
arr.insert(4,300)
print(arr)

#5 Extend python array using the extend() method
print("Step 5")
arr.extend([23,345,567,890])
print(arr)

#6 Add item from list into arr using from list() method
print("Step 6")
tempList=[1234,12345,123456]
arr.fromlist(tempList)
print(arr)

#7 remove any array element using remove() method
print("Step 7")
arr.remove(1234)
print(arr)

#8 remove elemt from array using pop () method
print("Step 8")
arr.pop()
print(arr)

#9 fetch any element from index
print("Step 9")
print(arr.index(300))

#10 reserve the array.

print("Step 10")
arr.reverse()
print(arr)


#11 buffer information through buffer_info method
print("Step 11")
print(arr.buffer_info())

#12 count element in array
print("Step 12")
print(arr.count(1))

#13 convert array to string
print("Step 13")
print(arr.__str__)

#14 covert array to list
print("Step 14")
print(arr.tolist())

# 15 slice the array
print("Step 15")
print(arr[:])


