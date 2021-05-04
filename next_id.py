"""
Hey awesome programmer!

You've got much data to manage and of course you use zero-based and non-negative ID's to make each data item unique!

Therefore you need a method, which returns the smallest unused ID for your next new data item...

Note: The given array of used IDs may be unsorted. For test reasons there may be duplicate IDs, but you don't have to find or remove them!

Go on and code some pure awesomeness!

def next_id(arr):    
    t = 0
    while t in arr:
        t +=1
    return t
         


"""

def next_id(arr):
    if arr == [] :return 0
    maximo = max(arr)
    numeros=[]
    numeros = [i for i in range(maximo+1)]
    
    for i in range(maximo+1):
        if numeros[i] not in arr:
            return numeros[i]

    return maximo +1
    

if __name__ =="__main__":
    print([0,1,2,3,4,5,6,7,8,9,10])