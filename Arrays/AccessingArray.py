from array import *

arr1 = array('i', [1,2,3,4,5,6])

def accessElement(array, index):
    if index >= len(array):
        print("there is not element with index")
    else:
        print(array[index])



accessElement(arr1, 6)
