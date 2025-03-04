
arr1 =[ 1,2,3,4,5]


def rotateLeft(d, arr):
    arr[:] = arr[d:] + arr[0:d]
    return arr




rotateLeft(2,arr1)

