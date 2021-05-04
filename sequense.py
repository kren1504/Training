def sequence(x):
    res=[]
    if x< 10:
        return [ i for i in range(1,x+1)]
    else:
        cantrep=x//10
        for i in range(cantrep):
            res.append(i+1)
            if x < ((i+2)*10):
                for j in range((i+1)*10,x+1):
                    res.append(j)
            else:
                for k in range((i+1)*10, (i+2)*10):
                    res.append(k)
        for i in range(cantrep+1,10):
            res.append(i)
        
    return res



if __name__ == "__main__":
    print(sequence(38))