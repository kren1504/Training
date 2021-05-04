"""
s = input()
distinctList = []
countList = []
for c in s:
    if c not in distinctList:
        distinctList.append(c)
for d in distinctList:
    count = s.count(d)
    countList.append(count)
#print(countList)
key = countList[0]
flags = 0
for count in countList:
    if(key != count):
        flags+=1
if(flags > 1):
    print("NO")
else:
    print("YES")

"""
def isValid(s):

    letrasCant = {}
    lista = []

    for letra in s:
        if letra not in letrasCant:
            letrasCant[letra] = s.count(letra)



    for key,item in letrasCant.items():
        if item not in lista:
            lista.append(item)

    print(letrasCant)
    lista.sort()
    print(lista)

    if len(lista) == 1 :return "YES"

    if len(lista) >= 3:
        return "NO"


    else: 
        #si hay mas de un item con numero diferente entonces return NO

        lista= lista[::-1]
        cont = 0

        for numero in lista:
            cont = 0
            for key,item in letrasCant.items():
                
            
                print("key",key, "item", item, " numero",numero)
                
                if numero == item :
                    cont += 1
                    print("cont",cont)
            
            if cont == 1 : return "YES"

            if cont > 1 : return "NO"

        return "YES"
                    


if __name__ == "__main__":
    print(isValid("aabbcd"))


