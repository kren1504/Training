def whatFlavors(money,arr):
    res = []
    flag = False
    for i in range(len(arr)-1):

        for j in range(len(arr)-1):

            if i != j :
                suma = arr[i] + arr[j]

                if suma == money:
                    res.append(i+1)
                    res.append(j+1)
                    flag= True
            
            if flag:
                break
            
        if flag :
            break
        
    print (res[0], res[1])
                



if __name__ == "__main__":
    print(whatFlavors(4,[2,2,4,3]))