"""
unction Description

Complete the sockMerchant function in the editor below.

sockMerchant has the following parameter(s):

    int n: the number of socks in the pile
    int ar[n]: the colors of each sock

Returns

    int: the number of pairs

Input Format

The first line contains an integer
, the number of socks represented in .
The second line contains space-separated integers,

, the colors of the socks in the pile.

Constraints

where

Sample Input

STDIN                       Function
-----                       --------
9                           n = 9
10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

Sample Output

3


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



"""


def sockMerchant(n, ar):
    dic = {}
    pares=0

    for ele in ar:
        if ele not in dic:
            dic[ele] = ar.count(ele)
        else:
            continue


    for key,item in dic.items():
        pares += item // 2
    
    return pares






if __name__== "__main__":
    print(sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20]))