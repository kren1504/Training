"""

In this Kata, you will be given two strings a and b and your task will be to return the characters that are not common in the two strings.

For example:

solve("xyab","xzca") = "ybzc" 
--The first string has 'yb' which is not in the second string. 
--The second string has 'zc' which is not in the first string. 

Notice also that you return the characters from the first string concatenated with those from the second string.

More examples in the tests cases.

Good luck!

"""
def uniqueStringCaracters(a,b):
    res = ""
    for element in a:
        if element not in b:
            res+=element
    
    for elemen in b:
        if elemen not in a:
            res += elemen

    return res

if __name__ =="__main__":
    print(uniqueStringCaracters("xyab","xzca"))