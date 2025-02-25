arr = [2,0,4,5,6,0]

def movezero(a):

   for i in range(len(a)):
       if a[i] == 0:
           print(a[i])

movezero(arr)