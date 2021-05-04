"""

Given a variable n,

If n is an integer, Return a string with dash'-'marks before and after each odd integer, but do not begin or end the string with a dash mark. If n is negative, then the negative sign should be removed.

If n is not an integer, return an empty value.

Ex:

dashatize(274) -> '2-7-4'
dashatize(6815) -> '68-1-5'


"""


def dashatize(n):
    if type(n) != int : return "None"
    
    if n <  0:
        n = n *(-1)
    n = str(n)
    res = ""
    
    for i in n:
        if int(i) % 2 != 0:
            res+= "-"+i+"-"
        else:
            res += i
            
    res =res.replace("--","-")

    return res.strip("-")
        

if __name__ == "__main__":
    print(dashatize(-123))