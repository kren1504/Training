#26 minutos

def word_mesh(a):
    res = ""
    j=0

    for i in range(len(a)-1):
        p1= a[i]
        p2= a[i+1]
        
        while j < len(p1):
            tamp1 = len(p1[j:])
        
            if p1[j:] in p2 and p1[j:] == p2[:tamp1]:
                res +=p1[j:]
                break
            j+=1
        else:
            return "failed to mesh"
        j=0

    return res







if __name__ == "__main__":
    print( word_mesh(["abandon", "donation", "onion", "ongoing"]))