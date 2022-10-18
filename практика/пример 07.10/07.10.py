x1, x2 = 0, 0
e = 2.718281828459045235360287471352662497

def f(x1, x2, e):
    return x1^2 + 2*x2^2 + e^(x1+x2)

def dfx1(x1, e):
    return 2*x1 + e^(x1+x2)

def dfx2(x2, e):
    return 4*x2 + e^(x1+x2)

def dfa(a, e):
    return 6*a - 2*a^(-2*a)

dfa(a, e)