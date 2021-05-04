"""
There is an array of strings. All strings contains similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'

Strings may contain spaces. Spaces is not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 3 strings.

This is the second kata in series:

$ python2.6 -m timeit '[x.lower() for x in ["A","B","C"]]'
1000000 loops, best of 3: 1.03 usec per loop
$ python2.6 -m timeit '[x.upper() for x in ["a","b","c"]]'
1000000 loops, best of 3: 1.04 usec per loop

$ python2.6 -m timeit 'map(str.lower,["A","B","C"])'
1000000 loops, best of 3: 1.44 usec per loop
$ python2.6 -m timeit 'map(str.upper,["a","b","c"])'
1000000 loops, best of 3: 1.44 usec per loop

$ python2.6 -m timeit 'map(lambda x:x.lower(),["A","B","C"])'
1000000 loops, best of 3: 1.87 usec per loop
$ python2.6 -m timeit 'map(lambda x:x.upper(),["a","b","c"])'
1000000 loops, best of 3: 1.87 usec per loop


my_set = {*a}
my_set
{'kljkf', 'asdasd'}
my_set = {*a[0]}

"""

def find_uniq(arr):
    if set(arr[0].lower()) == set(arr[1].lower()):
        majority_set = set(arr[0].lower())
    elif set(arr[0].lower()) == set(arr[2].lower()):
        majority_set = set(arr[0].lower())
    else:
        majority_set = set(arr[1].lower())
    
    for string in arr:
        if set(string.lower()) != majority_set:
            return string
            

    
    

if __name__ == "__main__":
    print(find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]))