"""

def LCS(s1, s2):
    n, m = len(s1), len(s2)
    lcs = [[0] * (m + 1) for _ in xrange(n + 1)]

    for i, c1 in enumerate(s1):
        for j, c2 in enumerate(s2):
            if c1 == c2:
                lcs[i][j] = lcs[i - 1][j - 1] + 1
            else:
                lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j])

    return lcs[n - 1][m - 1]


if __name__ == '__main__':
    a = raw_input()
    b = raw_input()

    print LCS(a, b)

"""


def LCS(X, Y,m,n):
	c = [[0] * (n+1) for i in range(m+1)]

	print(c,"c")

	for i in range(1, m+1):
		for j in range(1, n+1):

			print("i",i,"j",j)

			if X[i-1] == Y[j-1]: 
				c[i][j] = c[i-1][j-1] + 1

				print( " if  x", X[i-1],"y",Y[j-1]," cij ",c[i][j])

			else:
				c[i][j] = max(c[i][j-1], c[i-1][j])

	print(c,"c")
	return c[m][n]	






if __name__ == "__main__":
	print(LCS("ABCD","ABDC",4,4))