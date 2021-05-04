"""
    str = "ABC";  
    n = len(str);  
    #For holding all the formed substrings  
    arr = [];  
       
    #This loop maintains the starting character  
    for i in range(0,n):  
        #This loop will add a character to start character one by one till the end is reached  
        for j in range(i,n):  
            arr.append(str[i:(j+1)]);  
       
    #Prints all the subset  
    print("All subsets for given string are: ");  
    for i in arr:  
        print(i);  


from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

    if you don't like that empty tuple at the beginning, 
    you can just change the range statement to range(1, len(s)+1) to avoid a 0-length combination.

"""

# sub = []

# def calcularSubconjuntos(lista,acumulado):

#     if len(lista) == 1:
#         return sub.append(acumulado)

#     else:

#         for element in lista:

#             print(" lista -2 ",lista[1:]," acumulado", acumulado+element)
#             calcularSubconjuntos(lista[1:],acumulado+element )


    

def calcularSubconjuntos(s):

    n = len(s);  
    #For holding all the formed substrings  
    arr = [];  
       
    #This loop maintains the starting character  
    for i in range(0,n):  
        #This loop will add a character to start character one by one till the end is reached  
        for j in range(i,n):  
            arr.append(s[i:(j+1)])

    print(arr)

    return arr


def specialSubstring(s):
    cont =0 
    #sacar todas las sub cadenas del string y ver cuales cumplen los criterios y contarlos
    arr = calcularSubconjuntos(s)


    for element in arr:

        if len(element) == 2 and element[0] == element[1] :
            cont +=1
            print("1elemen",element)
            continue

        if len(element) == 1:
            #todos los elementos de un solo elemento
            print("2elemen",element)
            cont+=1
            continue

        if element.count(element[0]) == len(element): 
            # todos los elementos son iguales
            cont +=1
            print("3elemen",element)
            continue

        medio = (len(element)//2)
        if len(element) >=3 and element.count(element[0]) == (len(element)-1) and element[medio] != element[0] :
            
            print("4elemen",element)
            cont +=1
        
        medio = 0

    return cont


if __name__ == "__main__":
    print(specialSubstring("ccacacabccacabaaaabbcbccbabcbbcaccabaababcbcacabcabacbbbccccabcbcabbaaaaabacbcbbbcababaabcbbaaababababbabcaabcaacacbbaccbbabbcbbcbacbacabaaaaccacbaabccabbacabaabaaaabbccbaaaabacabcacbbabbacbcbccbbbaaabaaacaabacccaacbcccaacbbcaabcbbccbccacbbcbcaaabbaababacccbacacbcbcbbccaacbbacbcbaa"))