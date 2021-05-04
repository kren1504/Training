"""
Complete the function which accepts a string and return an array of character(s) that have the most spaces to their right and left.

Notes:

    the string can have leading/trailing spaces - you should not count them
    the strings contain only unique characters from a to z
    the order of characters in the returned array doesn"t matter

Examples

"a b  c"                        -->  ["b"]
"a bcs           d k"           -->  ["d"]
"    a b  sc     p     t   k"   -->  ["p"]
"a  b  c  de"                   -->  ["b", "c"]
"     a  b  c de        "       -->  ["b"]
"abc"                           -->  ["a", "b", "c"]


"""


def loneliest(strng):
    cizq= 0
    cder = 0
    res = []
    maximo=0
    aux = 0
    strng = strng.strip()
    
    for i in range(len(strng)):
        letraActual = strng[i]
        if strng[i].isalpha():
            aux = i-1
            while (aux > -1 ):
                if strng[aux] == " ":
                    cizq +=1
                    aux-=1
                else:
                    break
            i = i+1
            while ( i< len(strng)):
                if strng[i] == " ":
                    cder +=1
                    i +=1
                else:
                    break
            if cder + cizq > maximo:
                maximo = cder + cizq
                res = []
                res.append(letraActual)
                cizq = 0
                cder = 0
                continue


            if cder + cizq == maximo:
                res.append(letraActual)
            cizq = 0
            cder = 0

    return res

if __name__ == "__main__":
    print(loneliest("    a b  sc     p     t   k"))


                



