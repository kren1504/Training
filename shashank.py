
def alternatingCharacters(s):
    cont =0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            cont+=1


    return cont




if __name__ == "__main__":
    print(alternatingCharacters("BBBB"))