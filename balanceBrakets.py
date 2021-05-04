def isBalanced(s):
    stack = []
    stack.clear()

    openbrakets = "([{"

    dic = { ")":"(", "]":"[",
     "}":"{"}


    for i in s:

        if i in openbrakets:
            stack.append(i)
 
        else:

            if len(stack) >=1 and stack[-1] == dic[i]:
                stack.pop()
            else:
                return "NO"

    if stack == []:
        return "YES"
    else:
        return "NO"
    



if __name__ =="__main__":
    print(isBalanced(  "[()"   ))