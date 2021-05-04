"""
We want to approximate the sqrt function.
Usually this function takes a floating point number and returns another floating point number,
but in this kata we're going to work with integral numbers instead.

Your task is to write a function that takes an integer n and returns either

    an integer k if n is a square number, such that k * k == n or
    a range (k, k+1), such that k * k < n and n < (k+1) * (k+1).

Examples

sqrt_approximation(4) --> 2
sqrt_approximation(5) --> [2,3]


def sqrt_approximation(number):
    i = 0
    while i*i <= number:
        if i*i == number:
            return i
        i +=1
    else:
        return [i-1,i] 

"""

def sqrt_approximation(number):
    k=1
    while (k*k <= number):
        if k*k == number : return k
        k=k+1

    return [k-1,k]




if __name__ == "__main__":
    print(sqrt_approximation(4))