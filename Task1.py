from math import *
from mpmath import *
import numpy as np
mas1 = np.array([]); mas2 = np.array([]); mas3 = np.array([])
mas4 = np.array([]); mas5 = np.array([]); mas6 = np.array([])

def f(x, flag=False):
    if flag:
    print("""
    
    Функция, которая возвращает значение f(x)
    
    :params x: значение x

    :params func: заданная функция в типе str()

    :return: значение в точке x.
    
    """)
    
    try:
        a = eval(func)
    except ZeroDivisionError:
        a = inf
    return a


def fdx(x, h, func):
    
    """
    
    Функция, которая рассчитывает значение производной в конкретной точке методом двусторонней разности
    
    :params x: значение x

    :params h: шаг дифференцирования

    :params func: заданная функция в типе str()

    :return a: значение в дифференциале
    
    """
    
    try:
        a = (f(x + h, func) - f(x - h, func)) / (2 * h)
    except ZeroDivisionError:
        a = 0
    return a


def F(h, x, f):
    
    """
    
    Функция, которая рассчитывает значение интеграла в точке от x до x+шаг
    
    :params h: шаг дифференцирования

    :params func: заданная функция в типе str()

    :params x: значение x

    :return a: значение интеграла от x до (x+шаг)
    
    """
    
    try:
        a = (f(h) + f(x)) * (x - h) / 2
    except ZeroDivisionError:
        a = 0
    return a


def integ(a, b, step, func):  # рассчет интеграла и вывод результата
    
    """
    
    Функция, рассчитывающая интеграл от a до b

    :params a: нижний предел

    :params b: верхний предел

    :params step: шаг

    :params func: заданная функция в типе str()

    :return mas4: значение x
    
            mas5: значение интеграла в точке от x до x+шаг
            
            mas6: значение самой функции
            
    """
    
    inter = a + step
    mas4 = np.arange(int((b - a) / step) + 2)
    mas5 = np.arange(int((b - a) / step) + 2)
    mas6 = np.arange(int((b - a) / step) + 2)
    for i in range(1, int((b - a) / step)):  # (1)
        print('x =', round(inter, 3), 'f(x) =', round(f(inter, func), 3), "F(x) =", round(F(a, inter, func), 3))
        mas4[i] = inter
        mas5[i] = F(inter, step, func)
        mas6[i] = f(inter, func)
        inter = inter + step
    return mas4, mas5, mas6


def diff(a, b, step, func):  # рассчет дифференциала и вывод результата, когда a,b>0
    
    """
    
    Функция, рассчитывающая дифференциал от a до b

    :params a: нижний предел

    :params b: верхний предел

    :params step: шаг

    :params func: заданная функция в типе str()

    :return mas1: значение x
    
            mas2: значение производной в точке
            
            mas3: значение самой функции
            
    """
    
    inter = a
    mas1 = np.arange(int((b - a) / step) + 2)
    mas2 = np.arange(int((b - a) / step) + 2)
    mas3 = np.arange(int((b - a) / step) + 2)
    for i in range(1, int((b - a) / step) + 2):  # (1)
        print('x =', inter, 'f(x) =', f(inter, func), "f'(x) =", fdx(inter, step, func))
        mas1[i] = inter
        mas2[i] = fdx(inter, step, func)
        mas3[i] = f(inter, func)
        inter = inter + step
    return mas1, mas2, mas3


func = input('Введите функцию: ')
a = float(input('Введите нижний предел: '))
b = float(input('Введите верхний предел: '))
if isinstance(f(a), mpc) == True or f(a) == -inf:
    print('Ошибка: введеные значение не удовлетворяют области значений функции. Введите функцию заново')
else:
    if a > b:  # если предел a > b - это невозможно, выводим ошибку отправляем в начало.
        print('Ошибка ввода. Вы ввели неправильный предел. ')
    else:
        com = 'abc'
        while com != '0':  # чтобы команды спрашивались бесконечно, пока нормально не будут введены
            com = input(
                'Введите "1" для дифференцирования, введите "2" для интегрирования.\n "0" для выхода из программы ')
            if com == '1':
                h_o = int(input('Введите 1-шаг или 2-точность дифференцирования '))
                if h_o == 2:
                    step = float(input("Введите точность дифференцирования"))
                    step = step ** 2
                if h_o == 1:
                    step = float(input("Введите шаг дифференцирования"))
                if int(b - a) < step:
                    print('Ошибка ввода, шаг дифференцирования не может быть больше области дифференцирования.')
                else:  # если шаг меньше, и все хорошо, тогда выводим результат и забываем о существовании программы.
                    print(diff(a, b, step))
                    break
                break
            if com == '2':
                h_o = int(input('Введите 1-шаг или 2-точность интегрирования'))
                if h_o == 2:
                    step = float(input("Введите точность интегрирования"))
                    step = step ** 2
                if h_o == 1:
                    step = float(input("Введите шаг интегрирования"))
                if int(b - a) < step:
                    print('Ошибка ввода, шаг дифференцирования не может быть больше области интегрирования .')
                else:  # если шаг меньше, и все хорошо, тогда выводим результат и забываем о существовании программы.
                    print(integ(a, b, step))
                    break
                break
            else:
                print('Введена неправильная команда.')

def method_trap():
    s = 0.5*(f(a)+f(b))
    x = a+step
    while x <= b - step:
        s += f(x)
        x += step
    s = s*step
    return s
