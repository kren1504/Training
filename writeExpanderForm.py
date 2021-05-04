"""
 22 minutos
"""

def expand(num):

    res = []
    i=0
    while num > 0:
        
        if num%10 != 0:
        
            res.append( str((num%10)*(10**i)) )
        num = num // 10
        i+=1
    print(res)

    return " + ".join(res[::-1])


if __name__ == "__main__":
    print(expand(7005000))
