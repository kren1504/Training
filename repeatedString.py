

def repeatedString(s, n):
    
    tamTotal = len(s) * ( n //len(s))

    aAcumuladas = s.count("a") * (n // len(s))

    diferencia = tamTotal - n

    return aAcumuladas + s[:diferencia].count("a")




if __name__== "__main__":
    print(repeatedString("aba",6))