"""

Complete the solution so that the function will break up camel casing, using a space between words.
Example

solution("camelCasing")  ==  "camel Casing"



"""
def breakCamelCase(s):
    res = ""
    for letra in s:
        if letra.isupper():
            res += " "+letra
        else:
            res+=letra

    return res


if __name__ == "__main__":
    print(breakCamelCase("camelCasing"))