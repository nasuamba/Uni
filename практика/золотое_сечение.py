import math


def func(A, x):
    return pow(x, 4) + A[3]*pow(x, 3) + A[2]*pow(x, 2) + A[1]*x + A[0]

def golden_ratio(A, a, b, e):
    T = (3 - math.sqrt(5))/2
    x_1 = a + T*(b - a)
    x_2 = a + b - x_1
    l = 2*e; i = 0
    
    while l > e:
        f_1 = func([1, 2, 2, 1], x_1)
        f_2 = func([1, 2, 2, 1], x_2)
        if f_1 <= f_2:
            b = x_2
            x_2 = x_1
            x_1 = a + b - x_2
        elif f_1 > f_2:
            a = x_1
            x_1 = x_2
            x_2 = a + b - x_1

        l = b - a
        i += 1
    
    x = (a + b)/2
    f = func([1, 2, 2, 1], x_1)
    print(f'(.) минимума: {x}\nминимальное значение функции: {f}\n\nбыло найдено за {i} итераций')


golden_ratio([1, 2, 2, 1], -3, 2, 0.0001)