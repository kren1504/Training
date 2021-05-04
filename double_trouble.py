def trouble(x, t):
    res = []
    i=0
    print(x)
    while i  < (len(x)-1):
        if (x[i] + x[i+1])==t:
            valor = x[i+1]
            print("i ",i)
            print("xi", x[i], "xi+1",x[i+1])
            print("suma",x[i]+ x[i+1] ,"t",t,"valor",valor)
            del x[i+1]
            continue
        i+=1
        

    return x




if __name__== "__main__":
    print( trouble([1, 3, 5, 6, 7, 4, 3],7))