def backtrack(num, tam, vuelta,suma):

    if vuelta >= tam:
        print("vuelta tamano", vuelta," ", tam)

        return suma

    else:
        
        auxnum = num % 10
        num = num // 10

        print("auxnum ", auxnum," num ",num, " vuelta", vuelta, "tam",tam)
        return backtrack(num,tam,vuelta+1,suma+auxnum)
        




def sumaRecursiva(num):
    
    tam = len(num)
    num = int(num)
    return backtrack(num, tam, 0, 0)



if __name__ == "__main__":

    print(" resultando en main",sumaRecursiva("9875"))