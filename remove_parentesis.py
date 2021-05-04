"""

Remove the parentheses

In this kata you are given a string for example:

"example(unwanted thing)example"

Your task is to remove everything inside the parentheses as well as the parentheses themselves.

The example above would return:

"exampleexample"

Notes

    Other than parentheses only letters and spaces can occur in the string. Don't worry about other brackets like "[]" and "{}" as these will never appear.
    There can be multiple parentheses.
    The parentheses can be nested.



"""

def remove_parentheses(s):
    print(s)
    parentesis = []
    i=0

    while "(" in s or ")" in s:
        if s[i] == "(":
            parentesis.append(i)
        if s[i]== ")":
            s=s[:parentesis.pop()]+s[i+1:]
            i=0
            continue
        i+=1
        
    return s

if __name__ =="__main__":
    print(remove_parentheses("example(unwanted thing)exa(mpl)e"))