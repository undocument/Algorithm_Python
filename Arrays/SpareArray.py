

arr1 = ['aba', 'baba' , 'aba' , 'xzxb']
query1 = ['aba', 'xzxb' , 'ab' ]

def sparearray(list, query):

    frequency ={}

    for items in list:
           frequency[items] = frequency.get(items, 0) + 1

    result = [frequency.get(q, 0) for q in query]
    return result

print(sparearray(arr1, query1))
