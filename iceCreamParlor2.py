import time



def iceCreamParlor(n,a):

    res = []
    flag = False
    time.sleep(1)

    for i in range(len(a)):

        if flag == True :
            break

        for j in range(len(a)):

            if i!= j :
                if (a[i] + a[j]) == n:
                    res.append(str(i+1))
                    res.append(str(j+1))
                    flag = True
                    
    return " ".join(res)



def iceCreamChilli(money,arr):

    res= ""

    for i in range(len(arr)):

        

        resta = abs(money - arr[i])

        print("i ",i," arr[i] ",arr[i], " resta ", resta)

        aux = arr[i]

        arr[i] = -1

        if resta in arr and  (i != (arr.index(resta))):

            print(" rest in arr - i ", (i != (arr.index(resta))) )
            res += str(i+1)+ " "+ str((arr.index(resta))+1)
            break

        arr[i] = aux
            

    return res





if __name__ == "__main__":

    # starting time
    start = time.time()
    print(iceCreamChilli(4,[2,2,4,3]))
    # end time
    end = time.time()

    # total time taken
    print(f"Runtime of the program is {end - start}")

