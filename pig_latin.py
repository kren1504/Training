def pig_it(text):
    text = text.split(" ")
    res = []
    for ele in text:
        if ele.isalpha():
            res.append(ele[1:]+ ele[0]+"ay")
        else:
            res.append(ele)

    return " ".join(res)



if __name__=="__main__":
    print(pig_it('Pig latin is cool'))