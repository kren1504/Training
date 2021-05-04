def mark(a,budget):
    acumulado = 0
    cantJuguetes = 0


    a.sort()

    for ele in a:

        if ele + acumulado <= budget:
            acumulado += ele 
            cantJuguetes +=1

        

    return cantJuguetes





if __name__ == "__main__":

    print(mark([8,2,0,4],7))