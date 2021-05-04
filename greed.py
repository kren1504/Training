def score(dice):
    dic = {}
    res = 0
    cant = 0
    for num in dice:
        dic[num]=dice.count(num)

    for key,item in dic.items():
        cant = item
        while cant >=3:
            if key == 1:
                res += 1000
            else:
                res += key*100
            cant -=3
        
        if cant > 0  and key ==1:
            res += cant*100
        if cant > 0 and key ==5:
            res += cant*50

    return res


if __name__ == "__main__":
    print(score([4, 4, 4, 3, 3]))