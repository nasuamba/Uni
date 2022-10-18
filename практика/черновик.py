import math

def df(A, x):
    return 4*pow(x, 3) + 3*A[3]*pow(x, 2) + 2*A[2]*x + A[1]

A = [1, 2, 2, 1]
a = -3
b = 2

z = b - ((df(A, b)*(b-a))/(df(A, b) - df(A, a)))
print(z)
print(math.fabs(df(A, z)))
print(df(A, a))
print(df(A, b))