def separar(num):

    suma = 0
    print(num)

    for ele in num:

        suma += int(ele)


    return str(suma)




def superDigit(n):

    if len(n) ==1:
        return n

    else:

        numero = separar(n)
        print(numero)

        return superDigit(numero)




if __name__ == "__main__":
    print(" resultadooo ",superDigit('9875987598759875'))