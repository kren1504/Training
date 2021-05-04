"""
You are given an n by n ( square ) grid of characters, for example:

[['m', 'y', 'e'], 
 ['x', 'a', 'm'], 
 ['p', 'l', 'e']]

You are also given a list of integers as input, for example:

[1, 3, 5, 8]

You have to find the characters in these indexes of the grid if you think of the indexes as:

[[1, 2, 3], 
 [4, 5, 6], 
 [7, 8, 9]]

Remember that the indexes start from one and not zero.

Then you output a string like this:

"meal"

"""
def grid_index(grid, indexes):
    res = ""
    n = len(grid)
    for indice in indexes:
        pos = indice - 1
        fila = pos // n
        columna = ( pos - ((pos//n)*n))
        res += grid[fila][columna]

    return res
    

if __name__ == "__main__":
    print(grid_index([['m', 'y', 'e'],['x', 'a', 'm'], ['p', 'l', 'e']],[1, 3, 5, 8]))