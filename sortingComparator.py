
def sortingComparator(lista):

    aux = []

    for i in range(len(lista)):
        
        for j in range(len(lista)-1):
            
            if lista[j][1] < lista[j+1][1]:
                lista[j][0],lista[j+1][0] = lista[j+1][0], lista[j][0]
                lista[j][1],lista[j+1][1] = lista[j+1][1], lista[j][1]

            if lista[j][1] == lista[j+1][1]:
  

                if lista[j][0] > lista[j+1][0]:
                    lista[j][0],lista[j+1][0] = lista[j+1][0], lista[j][0]
                    lista[j][1],lista[j+1][1] = lista[j+1][1], lista[j][1]



    print ( lista)


    


#     d = {'one':1,'three':3,'five':5,'two':2,'four':4}
# a = sorted(d.items(), key=lambda x: x[1])    
# print(a)


    




if __name__ =="__main__":
    print(sortingComparator([["amy", 100], ["aaz", 100], ["ajjjj", 50], ["aakansha", 100], ["aleksa", 150]]))