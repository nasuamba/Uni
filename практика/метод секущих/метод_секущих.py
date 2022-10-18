import math

# Целевая функция
def f(A, x):
    return pow(x, 4) + A[3]*pow(x, 3) + A[2]*pow(x, 2) + A[1]*x + A[0]
# Производная
def df(A, x):
    return 4*pow(x, 3) + 3*A[3]*pow(x, 2) + 2*A[2]*x + A[1]


# Алгоритм поиска минимума методом секущих
def sec(A, a, b, e):
    z = 1
    i = 0
    while math.fabs(df(A, z)) > e:
        z = b - ((df(A, b)*(b-a))/(df(A, b) - df(A, a)))
        i += 1
        if df(A, a) < 0 or df(A, b) > 0: break

        if math.fabs(df(A, z)) <= e: break
        else:
            if df(A, z) > 0: a=z
            else: b=z
    
    opt_x = z
    opt_f = f(A, opt_x)
    print(f'(.) минимума: {opt_x}\nминимальное значение функции: {opt_f}\n\nбыло найдено за {i} итераций')


sec([1, 2, 2, 1], -3, 2, 0.000001)