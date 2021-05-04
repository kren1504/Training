
# Complete the minimumBribes function below.
def minimumBribes(n,q):
    cantSobornos = 0
    diferencia = 0

    

    if n != q.index(n)+1:


        diferencia = n - (q.index(n)+1)
        if diferencia > 0:
            cantSobornos += diferencia

    if cantSobornos >= 3 :
        return "Too caotic"

    else:
        return cantSobornos

    # for i in range(len(q)):
    #     if cantSobornos >= 3:
    #         break
    #     if q[i] != i+1:

    #     # if 
            
    #         diferencia = q[i]- (i+1)
    #         print("fuera de posicion ", q[i], " diferencia", diferencia)
    #         if diferencia > 0:
    #             cantSobornos += diferencia
    #             print("cant de sobornos +", cantSobornos)

    #     else:
    #         print("estoy en mi posicion")

    # if cantSobornos >= 3 :
    #     return "Too caotic"

    # else:
    #     return cantSobornos


if __name__ == "__main__":
    print(minimumBribes(8,[5 ,1 ,2 ,3 ,7 ,8 ,6,4]))