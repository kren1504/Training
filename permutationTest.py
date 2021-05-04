res = []

def permut(a,pos,tam):



    if pos == tam:
        res.append("".join(a))
        return

    else:
        

        for i in range(pos,tam):
                a[i],a[pos] = a[pos],a[i]
                permut(a,pos+1,tam)
                a[i],a[pos] = a[pos],a[i]



def bubble(num):

    tam = len(num)
    for i in range(tam):
        for j in range(tam-1):
            if num[j]> num[j+1]:
                num[j], num[j+1] = num[j+1],num[j]

    return num
    



if __name__ == "__main__":
    
    print(permut(list("abc"),0,len("abc")))
    print(res)

    print(bubble([10,5,48,60,100,30,1]))