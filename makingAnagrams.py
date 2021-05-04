"""

from collections import *    
a = Counter(raw_input())
b = Counter(raw_input())
c = a - b
d = b - a
e = c + d
print len(list(e.elements()))

"""



def makeAnagram(a,b):
    delection = 0

    i=0

    auxa = a[:]
    auxb = b[:]
    

    for letra in a:
        if letra not in b:
            auxa = auxa.replace(letra,"",1)
            delection +=1


    for letra in b:
        print("letra",letra)
        if letra not in a:
            print(auxb, " ",letra)
            auxb = auxb.replace(letra,"",1)
            print(auxb)
            delection +=1

    print("A", auxa, "B", auxb)

    if len(auxa) == len(auxb):

        return delection

    else:

        while( len(auxa) != len(auxb)):
            if auxa.count(auxa[i]) > auxb.count(auxa[i]):
                delection +=1
                auxa = auxa.replace(auxa[i],"",1)
                i=0

            elif auxa.count(auxa[i]) < auxb.count(auxa[i]):
                delection +=1
                auxb=auxb.replace(auxa[i],"",1)
                i=0
            else:
                i+=1

 
        return delection








if __name__ == "__main__":
    print(makeAnagram("fcrxzwscanmligyxyvym","jxwtrhvujlmrpdoqbisbwhmgpmeoke"))