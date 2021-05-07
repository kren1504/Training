""""
Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses
Examples

balanced_parens(0) => [""]
balanced_parens(1) => ["()"]
balanced_parens(2) => ["()()","(())"]
balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]



"""

res = []
validas = []

def permutacion(a,p,tam):
    
    if p == tam:
        if ("".join(a)) not in res:
            print("".join(a))
            res.append("".join(a))
        return
        
    else:
        
        for i in range(p,tam):
            a[i],a[p] = a[p],a[i]
            permutacion(a,p+1,tam)
            a[i],a[p] = a[p],a[i]
                
                
definitiva = []
def validas(a):
    stack=[]
    openbraket="("
    
    for elemento in a:
        

        if elemento in openbraket:
            stack.append(elemento)
            continue
        
        if len(stack)>=1 and stack[-1] == openbraket and elemento == ")":
            stack.pop()
            continue
            
        else:
            return
        
    if stack==[]:
        print("es valido",a)
        definitiva.append(a)
    else:
        return
        
     

def balanced_parens(n):
    brakets = "()"
    brakets*=n
    tam=len(brakets)
    print("brakets", brakets)
    brakets = list(brakets)
    print("brakets", brakets)
    permutacion(brakets,0,tam)
    print("res", res)
    for elemento in res:
        validas(elemento)
    return definitiva
    
if __name__ == "__main__":
    print(balanced_parens(3))