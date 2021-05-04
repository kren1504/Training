def sumOfDigits(num):

    if num == 0:

        return num

    else:

        return (( num % 10) + sumOfDigits( (num//10)))

def sumarDigitosDeNumero(num):
    suma = 0
    tam = len(str(num))
    for i in range(tam):
        suma += num % 10
        num = num //10
    return suma


def back(num,tamNum):

    if tamNum == 1:
        return num

    else:

        sumaTotal= sumOfDigits(num)

        return back(sumaTotal,len(str(sumaTotal)))
        

def superDigit(num,n):
    tam = len(num)
    num = int(num*n)
    return back(num,tam)




if __name__ == "__main__":
    print(superDigit( "123",3))