"""
Input Format

The first line contains an integer
, the total number of clouds. The second line contains space-separated binary integers describing clouds where

.

Constraints

Output Format

Print the minimum number of jumps needed to win the game.

Sample Input 0

7
0 0 1 0 0 1 0

Sample Output 0

4

Explanation 0:
The player must avoid
and . The game can be won with a minimum of jumps:

"""

def jumpingOnClouds(c):
    saltos = 0
    i=0
    while i  < len(c):
        print(" i ", i," len(c)",len(c))

        if  i+2 < len(c) and c[i+2] == 0:
            i+=2
            saltos +=1
            print("if ",i)

        else:
            i+=1

            saltos +=1
            print("else",i)

    return saltos



if __name__ =="__main__":
    print(jumpingOnClouds([0,0,1,0,0,1,0]))