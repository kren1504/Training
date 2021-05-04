
def canMakeTriangle(arr):
    res=[]
    
    for i in range(len(arr)-2):
        a = arr[i]
        b = arr[i+1]
        c = arr[i+2]
        
        if a+b > c and a+c>b and b+c>a:
            res.append(1)
        else:
            res.append(0)

    return res


if __name__ =="__main__":
    print(canMakeTriangle([1000000000, 1000000000, 1000000000, 1000000000]))