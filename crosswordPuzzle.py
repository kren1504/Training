
tablero = []

class coordenadas(self, f,c, esVertical, cantDeEspacio):
    def __init__(self,f,c,vertical):
        self.f = f
        self.c = c
        self.esVertical = esVertical
        self.cantDeEspacio = cantDeEspacio
        

def ColocarPalabra(palabra, tab):

    espaciosDisponibles()

    

def espaciosDisponibles( palabra, tab):
    coor = coordenadas()

    for i in range(10):
        for j in range(10):

            if tab[i][j] == "-":
                coor.f = i
                coor.c = j

                if tab[i+1][j] == "-" and i < 10:
                    coor.esVertical = True
                else
                    coor.esVertical = False

                if coor.esVertical :
                    while i < 10 and tab[i][j] == "-":
                        cantDeEspacios +=1
                        i +=1
                else:
                    while j < 10 and tab[i][j] == "-":
                        cantDeEspacios +=1
                        j +=1
                









def backtrack(posAct , arr, palabras,tab):

    if posAct == len(arr):
        tablero = tab
        return
    
    else:

        for palabra in palabras:

            tabaux = ColocarPalabra(palabra, tab)

            if tabaux == [[]]:
                continue
            else:
                backtrack( posAct+1, arr,palabras, tabaux)







def CrosswordPuzzle(arr, palabras):

    backtrack(0,arr, palabras ,[[]])

    return tablero









if __name__ == "__main__":
    print( CrosswordPuzzle( ))