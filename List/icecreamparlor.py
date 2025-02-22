m= 6
cost=[1,3,4,5,6]

def icecreamparlot(arr, m):


    for i , val in enumerate(arr):
        print(val)
        balance = m - val
        print(balance)
        if balance in arr:
            print(i,balance)



icecreamparlot(cost,m)