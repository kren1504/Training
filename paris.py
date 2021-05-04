"""
Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value. 
"""

def pairs(k, arr):
    a = set(arr)
    # make a set of all a[i] + k
    b = set(x + k for x in arr)
    # return the length of the intersection set
    return len(a&b)



def paris(k,arr):
    cont=0

    for i in range(len(arr)):

        for j in range(len(arr)):

            if i != j:
                if arr[i] - arr[j] == k:
                    cont +=1

    return cont




if __name__ == "__main__":
    print(paris(2,[1 ,5 ,3 ,4 ,2]))