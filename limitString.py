"""
The function must return the truncated version of the given string up to the given limit followed by "..." 
if the result is shorter than the original. Return the same string if nothing was truncated.

Example:

solution('Testing String', 3) --> 'Tes...'
solution('Testing String', 8) --> 'Testing ...'
solution('Test', 8)           --> 'Test'


"""

def solution(st, limit): 
    if len(st) < limit:
        return st
    else:
        return st[:limit]+"..."

if __name__ == "__main__":
    print(solution('Test', 4))