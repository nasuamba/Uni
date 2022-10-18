import numpy as np
import math

def f(a):
    '''целевая функция'''
    # 𝑓(𝑥1, 𝑥2) = 2(𝑥1)^2 + 5(𝑥2)^2 + (𝑥1)(𝑥2) − 3(𝑥1) − (𝑥2)
    return math.prod([2, (pow(a[0], 2))]) + math.prod([5, (pow(a[1], 2))]) + math.prod([a[0], a[1]]) - math.prod([3, a[0]]) - a[1]

def grad(a):
    '''записываем вектор градиента в массив'''
    return np.array([4*a[0] + a[1] - 3 , 10*a[1] + a[0] - 1])

def opt_a(A):
    '''решение задачи оптимизации для a (метод дихотомии)'''
    b1, b2 = -100, 100  # границы отрезка локализации минимума
    e = 0.0001          # точность вычеслений
    d = e / 2

    x1 = (b1 + b2 - d) / 2
    x2 = (b1 + b2 + d) / 2

    while (b2 - b1)/2 > e:
        if A(x1) > A(x2): b1 = x1
        else: b2 = x2
        x1 = (b1 + b2 - d) / 2
        x2 = (b1 + b2 + d) / 2
    a = (b2+b1)/2

    return a

def fastest_ClimbDown(e):
    '''метод наискорейшего спуска'''
    x = {}
    x[0] = [1, 1]   # начальная точка

    j = 0
    while (grad(x[0])[0]**2 + grad(x[0])[1]**2)**(1/2) > e:
        
        for i in range(len(x[0])):
            x[0][i] = x[0][i] - opt_a(lambda a: f(x[0] - a*grad(x[0])))*grad(x[0])[i]
            
        j += 1
        
        print(f'[{j}, [%0.3f; %0.3f], %0.3f, %0.3f]' % (x[0][0], x[0][1], f(x[0]), opt_a(lambda a: f(x[0] - a*grad(x[0]))) ))
        
    print('')
    print('оптимальное значение х = [%0.3f; %0.3f]' % (x[0][0], x[0][0]))
    print('оптимальное значение f(х) = %0.3f' % (f(x[0])))




fastest_ClimbDown(0.0001)
