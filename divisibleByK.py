def divisibleByK(arr,k):

    cont = 0

    vuelta = 0

    arr.sort()


    while vuelta < (len(arr)):
        for j in range(vuelta,len(arr)):

            print(arr[vuelta]," ",arr[j])

            if arr[vuelta] < arr[j] :
                if (arr[vuelta]+ arr[j]) % k == 0:
                    cont+=1

            else:
                continue
        vuelta+=1

    return cont







if __name__ == "__main__":
    print(divisibleByK([10,2,8,4,5],3))