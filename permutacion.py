
 
resul  =[]
 

def permute(a, l, r):
    if l==r:
        "".join(a)
        resul.append("".join(a))

        
    else:
        for i in range(l,r):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]

# This code is contributed by Bhavya Jain


string = "abcd"
n = len(string)
a = list(string)
b = a[:]
resul.clear()

permute(a, 0, n)
cont = 0
print("")
print(resul)
