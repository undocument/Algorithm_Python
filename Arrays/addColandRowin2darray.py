import numpy as np

twoDArray = np.array([[1,2,3,4],[10,11,12,13],[12,23,34,45],[23,45,78,90]])
print(twoDArray)

new2arr = np.insert(twoDArray,0, [[2,0,5,6]], axis=1)
print(new2arr)


