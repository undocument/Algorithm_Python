

import numpy as np


twoDArray = np.array([[1,2,3,4],[10,11,12,13],[12,23,34,45],[23,45,78,90]])
print(twoDArray)


def traverseArray(array):
    for i in range (len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


traverseArray(twoDArray)