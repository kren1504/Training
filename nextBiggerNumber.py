res = []

 
# Function to print permutations of string
# This function takes three parameters:
# 1. String
# 2. Starting index of the string
# 3. Ending index of the string.
def permute(a, l, r):
    if l==r:
        res.append(int( "".join(a)))
        
    else:
        for i in range(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack

    return res
 



def nextBigger(num):

    snum = str(num)
    n = len(snum)
    a = list(snum)


    arr = permute(a,0,n-1)

    arr.sort()

    for ele in arr :
        if ele > num:
            return ele
    
    return -1

def substring(num):
    tam = len(str(num))
    num = str(num)
    listaNum = []

    for i in range(tam):

        for j in range(i,tam):

            listaNum.append( int ( num[i:(j+1)]))

    return listaNum

if __name__ == "__main__":
    print ( nextBigger( 513))
