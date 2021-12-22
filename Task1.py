try:
    import math
except ModuleNotFoundError:
    install("math")
try:
    import matplotlib.pyplot
except ModuleNotFoundError:
    install("matplotlib.pyplot")
try:
    import numpy
except ModuleNotFoundError:
    install("numpy")
try:
    import time
except ModuleNotFoundError:
    install("time")
try:
    import mpmath
except ModuleNotFoundError:
    install("mpmath")

from math import *
import matplotlib.pyplot as plt
from numpy import array
import numpy as np
import time
from mpmath import *


def f(x):
    try:
        a = eval(func)
    except ZeroDivisionError:
        a = inf
    return a


def fdx(x, h):  # рассчет дифференциала от значения x с шагом
    try:
        func = (f(x + h) - f(x - h)) / (2 * h)
    except ZeroDivisionError:
        func = inf
    return func


def integ(a, b, step):  # рассчет интеграла и вывод результата
    k = 0
    inter = a
    plt.title("Графики функций f(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()  # сеточка
    # plt.scatter(mpf(inter),mpf(f(inter)), label = "f(x)", color='b') # легенда для графика функции

    # так как мы используем метод трапеций, то будем выводить сумму значений функций в точках на промежутке
    s = 0
    s = float()
    s = mpf(f(inter)) * 0.5
    if (f(inter) != inf and f(inter) != -inf):
        plt.scatter(mpf(inter), mpf(f(inter)), color='b')
    print('x =', mpf(inter), 'f(x) = ', mpf(f(inter)), "s=", s)
    inter = round((inter + step), len(str(step)))
    for i in range(1, int((b - a) / step)):  # (1)
        s = s + mpf(f(inter))
        print('x =', mpf(inter), 'f(x) =', mpf(f(inter)), "s=", s)
        if (f(inter) != inf and f(inter) != -inf):
            if k == 0:
                k = 1
                plt.scatter(mpf(inter), mpf(f(inter)), label="f(x)", color='b')  # легенда для графика функции
            else:
                plt.scatter(mpf(inter), mpf(f(inter)), color='b')
        inter = round((inter + step), len(str(step)))
    if (f(inter) != inf and f(inter) != -inf):
        plt.scatter(mpf(inter), mpf(f(inter)), color='b')
    plt.legend()
    s = s + mpf(f(inter)) * 0.5
    print('x =', mpf(inter), 'f(x) =', mpf(f(inter)), "s=", s)
    s = s * step
    print("Значение интеграла", s)
    plt.show()
    return ('Интегрирование завершено.')


def diff(a, b, step):  # рассчет дифференциала и вывод результата, когда a,b>0
    k = 0
    inter = a  # шаг итерации функции или как это называется я хз
    plt.plot()
    plt.title("Графики функций f(x), f'(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid()  # сеточка
    # plt.scatter(mpf(inter),mpf(fdx(inter, step)), label = "f'(x)",color = 'g') # легенда для графика производной
    # plt.scatter(mpf(inter),mpf(f(inter)), label = "f(x)", color='b') # легенда для графика функции
    # plt.legend()
    for i in range(1, int((b - a) / step) + 2):  # (1)
        print('x =', mpf(inter), 'f(x) =', mpf(f(inter)), "f'(x) =", mpf(fdx(inter, step)))
        if (f(inter) != inf and f(inter) != -inf and fdx(inter, step) != inf and fdx(inter, step) != -inf):
            if k == 0:
                k = 1
                plt.scatter(mpf(inter), mpf(fdx(inter, step)), label="f'(x)", color='g',
                            s=5)  # легенда для графика производной
                plt.scatter(mpf(inter), mpf(f(inter)), label="f(x)", color='b', s=5)  # легенда для графика функции
            else:
                plt.scatter(mpf(inter), mpf(fdx(inter, step)), color='g', s=5)
                plt.scatter(mpf(inter), mpf(f(inter)), color='b', s=5)

        inter = round((inter + step), len(str(step)))
    plt.legend()
    plt.show()
    return ('Дифференцирование завершено.')


func = input('Введите функцию: ')
a = float(input('Введите нижний предел: '))
b = float(input('Введите верхний предел: '))
if (isinstance(f(a), mpc) == True or f(a) == -inf):
    print('Ошибка: введеные значение не удовлетворяют области значений функции. Введите функцию заново')
else:
    if (a > b):  # если предел a > b - это невозможно, выводим ошибку отправляем в начало.
        print('Ошибка ввода. Вы ввели неправильный предел. ')
    else:
        com = 'abc'
        while com != '0':  # чтобы команды спрашивались бесконечно, пока нормально не будут введены
            com = input(
                'Введите "1" для дифференцирования, введите "2" для интегрирования.\n "0" для выхода из программы ')
            if com == '1':
                h_o = int(input('Введите 1-шаг или 2-точность дифференцирования '))
                if (h_o == 2):
                    step = float(input("Введите точность дифференцирования"))
                    step = step ** 2
                if (h_o == 1):
                    step = float(input("Введите шаг дифференцирования"))
                if (
                        int(b - a) < step):  # если шаг больше, чем область дифф-ия, то тогда выводим ошибку и отправляем в начало
                    print('Ошибка ввода, шаг дифференцирования не может быть больше области дифференцирования.')
                else:  # если шаг меньше, и все хорошо, тогда выводим результат и забываем о существовании программы.

                    print(diff(a, b, step))
                    break
                break
            if com == '2':
                h_o = int(input('Введите 1-шаг или 2-точность интегрировния'))
                if (h_o == 2):
                    step = float(input("Введите точность интегрировния"))
                    step = step ** 2
                if (h_o == 1):
                    step = float(input("Введите шаг интегрировния"))
                if (
                        int(b - a) < step):  # если шаг больше, чем область дифф-ия, то тогда выводим ошибку и отправляем в начало
                    print('Ошибка ввода, шаг дифференцирования не может быть больше области интегрирования .')
                else:  # если шаг меньше, и все хорошо, тогда выводим результат и забываем о существовании программы.

                    print(integ(a, b, step))
                    break
                break
            else:
                print('Введена неправильная команда.')

#вычисление времени работы функций в точке а (дифференцирование)
try:
    import scipy.misc
except ModuleNotFoundError:
    install("scipy.misc")
from scipy.misc import derivative
print("Для встроенной функции:")
start = time.perf_counter_ns()
derivative(f,a)
end = time.perf_counter_ns()
print(f"Время выполнения = {end - start}")
print("Для написанной функции:")
start = time.perf_counter_ns()
fdx(a, step)
end = time.perf_counter_ns()
print(f"Время выполнения = {end - start}")


def trap():
    s=0.5*(f(a)+f(b))
    x=a+step
    while x <= b - step:
        s += f(x)
        x += step
    s=s*step
    return s
