

def getMinimumCost(k, c):
    c.sort()
    c = c[::-1]
    minimunCost = 0
    vuelta = 1

    for i in range(k):
        
        minimunCost += c[i]
        print("i",i,"MC", minimunCost," c[i] ",c[i])
    
    for j in range(k,len(c)):
        minimunCost += (vuelta + 1) * c[j]
        print("j", j,"MC", minimunCost," c[j] ",c[j], "vuelta", vuelta)

        if vuelta >= k:
            vuelta +=1
            

    return minimunCost



if __name__ == "__main__":
    print(getMinimumCost(2,[6,5,2]))