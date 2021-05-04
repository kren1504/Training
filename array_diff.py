"""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b.

def array_diff(a, b):
    seta = set(a)
    setb = set(b)

    return list( seta-setb)

"""

def array_diff(a, b):
    res = []

    for elea in a:
        if elea not in b:
            res.append(elea)

    return res
    

if __name__=="__main__":
    print(array_diff([1,2,2,2,3],[2]))
