def switcheroo(string):
    res = ""
    for i in string:
        if  i == "a":
            res+= "b"
        elif i == "b":
            res+="a"
        else:
            res+="c"
    return res
        

if __name__ == "__main__":
    print(switcheroo('aaabcccbaaa'))