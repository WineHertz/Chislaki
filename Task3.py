import numpy as np
import random
import math
import copy
from fractions import Fraction


def com(s):
    """
    Функция, которая преобразует комплексное число в правильный вид
    :params s: введенное число(строка)
    :return s_new: преобразованное число(строка)
    """
    s_new = ''
    k = []
    for i in range(len(s)):
        k.append(s[i])
    l = 0
    for i in range(len(k)):
        if k[i] == '-':
            l = i
    for i in range(l, len(k)):
        s_new += k[i]
    s_new += '+'
    for i in range(l):
        s_new += k[i]
    return s_new
def comm(s):
    """
    Функция, которая преобразует комплексное число в правильный вид
    :params s: введенное число(строка)
    :return s_new: преобразованное число(строка)
    """
    s_new = ''
    k = []
    for i in range(len(s)):
        k.append(s[i])
    l = 0
    for i in range(len(k)):
        if k[i] == '+':
            l = i
    for i in range(l,len(k)):
        s_new += k[i]
    s_new += '+'
    for i in range(l):
        s_new += k[i]
    return s_new

def input_of_matrix():
    """
    Функция, которая позволяет ввести матрицу с клавиатуры
    :return matrix: введенная матрица
    """
    while True:
        try:
            columns, rows = map(int, input('\nРазмер матрицы составляет:\nКоличество столбцов и строк:\t').split())
            if columns > 0 and rows > 0 and columns == rows + 1:
                break
            else:
                 print('\nВведите правильно количество столбцов и строк')
        except ValueError:
            print('\nВводите только числа, превышающие 0')
    matrix = []
    list_of_rows = []
    for i in range(rows):
        while True:
            list_of_rows = list(input().split())
            if len(list_of_rows) != columns:
                print('Введите корректное количество')
            else:
                break
        matrix.append(list_of_rows)
    for i in range(rows):
        for j in range(columns):
            if 'j-' in matrix[i][j]:
                matrix[i][j] = complex(com(matrix[i][j]))
            elif 'j+' in matrix[i][j]:
                matrix[i][j] = complex(comm(matrix[i][j]))
    for i in range(rows):
        for j in range(columns):
            try:
                if matrix[i][j].isdigit():
                    try:
                        matrix[i][j] = int(matrix[i][j])
                    except AttributeError:
                        pass
            except AttributeError:
                pass
            else:
                try:
                    matrix[i][j] = matrix[i][j]
                except ValueError:
                    pass
    for i in range(rows):
        for j in range(columns):
            try:
                if "." in matrix[i][j]:
                    try:
                        matrix[i][j] = float(matrix[i][j])
                    except TypeError:
                        pass
            except TypeError:
                pass
    for i in range(rows):
        print('\n')
        for j in range(columns):
            print(matrix[i][j], end = '\t')
    return matrix

def minor(A, i, j):
    """
    Функция, которая считает минор матрицы
    :params A: матрица
    :params i: строка, которая удалится
    :params j: столбец, который удалится
    :return M: минор
    """
    M = copy.deepcopy(A)
    del M[i]
    for i in range(len(A[0]) - 1):
        del M[i][j]
    return M


def det(A):
    """
    Функция, которая считает определитель матрицы
    :params A: матрица
    :return determinant: определитель матрицы
    """
    m = len(A)
    n = len(A[0])
    if m != n:
        return None
    if n == 1:
        return A[0][0]
    signum = 1
    determinant = 0
    # разложение по первой строке
    for j in range(n):
        determinant += A[0][j] * signum * det(minor(A, 0, j))
        signum *= -1
    return determinant


def opr_vv_m(a):
    """
    Функция, которая считает определитель введенной матрицы
    :params a: введенная матрица
    :return det(matrix): определитель введенной матрицы
    """
    matrix = a
    print()
    print('Определитель введенной матрицы равен')
    return det(matrix)

def generator_of_matrix():
    """
    Функция, которая выводит сгенерированную матрицу
    :return matrix: сгенерированная матрица
    """
    while True:
        try:
            columns, rows = map(int, input('\nРазмер матрицы составляет:\nКоличество столбцов и строк:\t').split())
            if columns > 0 and rows > 0:
                break
        except ValueError:
            print('\nВводите только числа, превышающие 0')
    matrix = [[random.randint(-100, 100) for j in range(columns)] for i in range(rows)]
    return matrix


def jacobi(matrix):
    """
    Функция, которая решает СЛАУ методом Якоби
    :params matrix: матрица
    """
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            for j in range(len(matrix)):
                if j != i and matrix[j][i] != 0:
                    matrix[i] = [matrix[i][k] + matrix[j][k] for k in range(len(matrix) + 1)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                matrix[i] = [matrix[i][k] / matrix[i][i] for k in range(len(matrix) + 1)]
    b = []
    a = []
    for i in range(len(matrix)):
        b.append(matrix[i][-1:])
        a.append(matrix[i][:-1])
    b = [lst[0] for lst in b]

    def isCorrectArray(a):
        """
        Функция, которая проверяет коэффициента матрицы на их корректность
        :params a: матрица
        """
        for row in range(0, len(a)):
            if (len(a[row]) != len(b)):
                print('Не соответствует размерность')
                return False
        return True


    def isNeedToComplete(x_old, x_new):
        """
        Условие завершения программы на основе вычисления расстояния между соответствующими элементами
        соседних итераций
        :params x_old: предыдущая итерация
        :params x_new: новая итерация
        :return math.sqrt(sum_up / sum_low) < eps: True or False, условие завершения программы
        """
        eps = 0.0001
        sum_up = 0
        sum_low = 0
        for k in range(0, len(x_old)):
            sum_up += (x_new[k] - x_old[k]) ** 2
            sum_low += (x_new[k]) ** 2

        return math.sqrt(sum_up / sum_low) < eps


    def solution(a, b):
        """
        Процедура решения
        :params a: матрица коэффициентов
        :params b: матрица свободных членов
        :return: матрица решений x
        """
        if (not isCorrectArray(a)):
            print('Ошибка в исходных данных')
        else:
            count = len(b)  # количество корней

            x = [1 for k in range(0, count)]  # начальное приближение корней

            numberOfIter = 0
            MAX_ITER = 100
            while (numberOfIter < MAX_ITER):

                x_prev = copy.deepcopy(x)

                for k in range(0, count):
                    S = 0
                    for j in range(0, count):
                        if j != k:
                            S = S + a[k][j] * x[j]
                    x[k] = b[k] / a[k][k] - S / a[k][k]

                if isNeedToComplete(x_prev, x):
                    break

                numberOfIter += 1
            print()
            print('Количество итераций на решение: ', numberOfIter)

            return x


def gauss_jord(matrix):
    """
    Функция, которая решает СЛАУ прямым методом Жордана-Гаусса
    :params matrix: расширенная матрица
    :return: матрица решений x, матрица коэффициентов, обратная матрица коэффициентов
    """
    b = []
    a = []
    for i in range(len(matrix)):
        b.append(matrix[i][-1:])
        a.append(matrix[i][:-1])
    b = [lst[0] for lst in b]
    x = [[0] for _ in range(len(matrix))]

    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            for j in range(len(matrix)):
                if j != i and matrix[j][i] != 0:
                    matrix[i] = [matrix[i][k] + matrix[j][k] for k in range(len(matrix) + 1)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                matrix[i] = [matrix[i][k] / matrix[i][i] for k in range(len(matrix) + 1)]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                ratio = matrix[j][i] / matrix[i][i]
                for k in range(len(matrix) + 1):
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

    for i in range(len(matrix)):
        x[i] = matrix[i][len(matrix)] / matrix[i][i]
    return x, a, np.linalg.inv(a)


def gauss_jord_rational(matrix):
    """
    Функция, которая решает СЛАУ методом Жордана-Гаусса с дробями
    :params matrix: расширенная матрица
    :return: решения x
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = Fraction(matrix[i][j])

    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            for j in range(len(matrix)):
                if j != i and matrix[j][i] != 0:
                    matrix[i] = [matrix[i][k]+matrix[j][k] for k in range(len(matrix)+1)]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                matrix[i] = [matrix[i][k]/matrix[i][i] for k in range(len(matrix)+1)]
    x = [[0] for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                ratio = matrix[j][i] / matrix[i][i]
                for k in range(len(matrix) + 1):
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

    for i in range(len(matrix)):
        x[i] = matrix[i][len(matrix)] / matrix[i][i]
    print('\nПолученное решение: ')
    for i in range(len(matrix)):
        print(f'X{i} = {Fraction(x[i]).numerator}/{Fraction(x[i]).denominator} = {round(Fraction(x[i]), 2)}')

def main(matrix):
    """
    Главная функция порядка вызова других функций
    :params matrix: расширенная матрица
    :return: решения СЛАУ различными методами
    """
    delta = 0.001
    b = []
    a = []
    for i in range(len(matrix)):
        b.append(matrix[i][-1:])
        a.append(matrix[i][:-1])
    b = [lst[0] for lst in b]
    linalg_matrix = []
    for i in range(len(matrix)):
        linalg_matrix.append(matrix[i][:-1])
    determinant = opr_vv_m(linalg_matrix)
    cord = np.linalg.cond(linalg_matrix)
    if abs(determinant) <= delta:
        if abs(np.linalg.det(linalg_matrix))<=delta:
            print('Матрица вырожденная, система не имеет решений')
        else:
            print()
            print('Решение СЛАУ методом Якоби')
            try:
               jacobi()
            except OverflowError:
                print('Решение СЛАУ методом Жордана-Гаусса')
                gauss_jord()
                print()
                print('Решение СЛАУ методом Жордана-Гаусса с дробями')
                gauss_jord_rational()
            if cord < 100:
                print('Решение закончено')
            else:
                print()
                print('Решение СЛАУ методом Жордана-Гаусса')
                gauss_jord()
                print()
                print('Решение СЛАУ методом Жордана-Гаусса с дробями')
                gauss_jord_rational()
                print('Решение закончено')