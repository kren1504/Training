
"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:

"""

def find_uniq(arr):
    
    arr = list(map(str,arr))
    arr.sort()
    if arr[0] == arr[1]:
        return arr[-1]
    else:
        return arr[0]

if __name__ == "__main__":
    print(find_uniq([ 4, 4, 'foo', 4 ]))