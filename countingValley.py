def countValley(steps, path):
    NIVELDELMAR = 0
    alturaActual = 0
    entrasteEnValle = False
    cantValles = 0 

    for letra in path:
        if letra == "U":
            alturaActual +=1

        if letra =="D":
            alturaActual -=1

        if alturaActual < 0 :
            entrasteEnValle = True

        if alturaActual == NIVELDELMAR and entrasteEnValle :
            cantValles +=1
            entrasteEnValle = False
            


    return cantValles



if __name__== "__main__":
    print(countValley(8,"UDDDUDUU"))