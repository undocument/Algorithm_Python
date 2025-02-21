arr1 = [-4, 3, -9, 0, 4, 1]

def plusMinus(arr):

    post_count =sum(1 for i in arr if i > 0)
    neg_count = sum(1 for i in arr if i < 0)
    zero_count = sum(1 for i in arr if i == 0)

    print(post_count/len(arr))
    print(neg_count/len(arr))
    print(zero_count/len(arr))


plusMinus(arr1)





