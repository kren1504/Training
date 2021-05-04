""" 
Write Number in Expanded Form

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'


"""

def expandedForm(num):
    res = []
    cont=0

    while num > 0:
        aux = num %10
        num = num // 10
        cont +=1
        if aux == 0 :
            continue
        res.append(str(aux*(10)**(cont-1)))
        

    res=res[::-1]
    return " + ".join(res)

if __name__ == "__main__":
    print(expandedForm(70304))