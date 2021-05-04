def div_con(x):
    nonintegers= 0
    integers = 0
    for ele in x:
        if type(ele) == int:
            integers += ele
        else:
            nonintegers += int(ele)

    return integers - nonintegers


if __name__ =="__main__":
    print(div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7]))