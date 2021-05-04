
def countSwaps(a):
    contador = 0
    for i in range(len(a)):
        
        for j in range(len(a)-1):
            
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1], a[j]
                contador +=1
                
    print(a)
    print ( contador, a[0], a[-1])
                
    




if __name__ =="__main__":
    print(countSwaps ([5,4,3,8,6,1]))