#remove duplicate with extra space

a = [0,0,1,1,1,2,2,3,3,4]

def removeDuplicate(arr):
    newlst=[]
    for i in arr:
        if i not in newlst:
            newlst.append(i)
    return len(newlst)




print(removeDuplicate(a))