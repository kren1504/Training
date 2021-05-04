def tripleSum(a,b,c):
    repetidos = []

    cont= 0

    for p in a:
        for q in b:
            if p <= q:
                for r in c:

                    if q>=r:
                        aux = str(p)+str(q)+str(r)
                        if aux not in repetidos:
                            repetidos.append(aux)
                            cont+=1
                            aux = ""

    return cont

    


if __name__ == "__main__":
    print(tripleSum([1,4,5], [2,3,3], [1,2,3]))
