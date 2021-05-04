# Complete the rotLeft function below.



"""
def solve(a, d):
	return(a[d:]+a[:d])
"""
def rotLeft (d,a):
    x=a+a

    return x[d:d+len(a)]
    
    
    

if __name__ == "__main__":
    print(rotLeft(4,[1,2,3,4,5,6]))