
conteo = 0

def stepPerms(cantDePasos,escalones):
    
    if cantDePasos == escalones:
        global conteo
        conteo +=1
        return
    
    else:
        for i in range(0,3): # cantidad de pasos que puedo dar, hasta 3 pasos
            if (cantDePasos +i+1 )<= escalones:
                stepPerms(cantDePasos+ i+1,escalones)
            else:
                break
        return


if __name__ == "__main__":

    stepPerms(0,3)

    print("conteo global", conteo)
