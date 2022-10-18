import math

import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update(x, y, x_new, y_new, ax):
    x.append(x_new)  # update data
    y.append(y_new)

    ax.relim()  # update axes limits
    ax.autoscale_view(True, True, True)
    return x, y


# Целевая функция
def func(A, x):
    return pow(x, 4) + A[3]*pow(x, 3) + A[2]*pow(x, 2) + A[1]*x + A[0]

def check(a, b, x_1, x_2, f_1, f_2):
    if f_1 <= f_2:
        b = x_2
        x_2 = x_1
        x_1 = a + b - x_2
    elif f_1 > f_2:
        a = x_1
        x_1 = x_2
        x_2 = a + b - x_1

# Алгоритм поиска минимума методом золотого сечения
def golden_ratio(A, a, b, e):
    T = (3 - math.sqrt(5))/2
    x_1 = a + T*(b - a)
    x_2 = a + b - x_1

    # первая итерация
    f_1 = func(A, x_1)
    f_2 = func(A, x_2)
    if f_1 <= f_2:
        b = x_2
        x_2 = x_1
        x_1 = a + b - x_2
    elif f_1 > f_2:
        a = x_1
        x_1 = x_2
        x_2 = a + b - x_1
    l = b - a
    i = 1

    while l > e:
        # график
        x = [x_1, x_2]
        y = [f_1, f_2]
        fig, ax = plt.subplots()

        ani = animation.FuncAnimation(fig, update(x, y, x_1, x_2, ax))
        plt.show()
        
        if f_1 <= f_2:
            f_2 = f_1
            f_1 = func(A, x_1)
            if f_1 <= f_2:
                b = x_2
                x_2 = x_1
                x_1 = a + b - x_2
            elif f_1 > f_2:
                a = x_1
                x_1 = x_2
                x_2 = a + b - x_1
        elif f_1 > f_2:
            f_1 = f_2
            f_2 = func(A, x_2)
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
    f = func(A, x_1)
    print(f'(.) минимума: {x}\nминимальное значение функции: {f}\n\nбыло найдено за {i} итераций')


golden_ratio([1, 2, 2, 1], -3, 2, 0.000001)