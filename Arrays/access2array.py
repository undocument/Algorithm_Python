import numpy as np
from numpy.ma.core import arange

twoDArray = np.array([[1,2,3,4],[10,11,12,13],[12,23,34,45],[23,45,78,90]])
print(twoDArray)


def accessElement(array, rowindex , colindex):
    if rowindex >= len(array) and colindex >= len(array[0]):
        print('Incoorect index')
    else:
        print(array[rowindex][colindex])



accessElement(twoDArray,1,2)




