def maxMin(k, arr):

    minimo = 100001

    arr.sort()
    aux = []
    j = k


    for i in range(len(arr)-k+1):

            aux = arr[i:j]

            print(j,"j",k,"k ",aux)

            if max(aux) - min(aux) <= minimo:
                minimo = max(aux) - min(aux)


            aux = []
            j +=1

    return minimo

            

            


if __name__ == "__main__":
    print(maxMin(3,[10,100,300,200,1000,20,30]))
