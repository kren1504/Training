def get_consective_items(items, key): 
    maximo = 0
    cont = 0 
    flag = True
    elementos = str(items)
    clave = str(key)
    if clave not in elementos: return 0
    
    for i in range(len(elementos)):
        if elementos[i] == clave:
            print("clave")
            cont +=1
            flag = True
        else:
            print("no clave")
            flag = False
        if cont > maximo:
            maximo = cont
            
        if flag == False:
            cont=0
        
    return maximo

if __name__ == "__main__":
    print(get_consective_items(90000, 0))