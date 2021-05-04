def readingVertically(arr):
    res = ""
    cantVueltas = 0

    tamanos = map(len, arr)

    maximo = max(tamanos)


    while cantVueltas != maximo:

        for palabra in arr:

            if cantVueltas < len(palabra):
                res+=palabra[cantVueltas]

        cantVueltas +=1

    return res



if __name__ == "__main__":
    print(readingVertically(["e","M","y","l","y"]))