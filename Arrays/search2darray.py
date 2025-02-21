import numpy as np


twoDArray = np.array([[1,2,3,4],[10,11,12,13],[12,23,34,45],[23,45,78,90]])


def search2array(arr, value):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == value:
                return 1
    return -1

print(search2array(twoDArray, 90))