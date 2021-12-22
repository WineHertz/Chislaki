import numpy as np
import copy
import random

def see_matrix(matrix):
    for row in matrix:
        print(*row)


def input_of_matrix():
    """
    Функция, которая позволяет ввести матрицу с клавиатуры
    :return matrix: введенная матрица
    """
    while True:
        try:
            columns, rows = map(int, input('Размер матрицы составляет:\nКоличество столбцов и строк:\t').split())
            if columns > 0 and rows > 0:
                break
            else:
                print('Вводите числа, больше 0')
        except ValueError:
            print('Вводите только числа')

    print()

    matrix = []
    for i in range(rows):
        flag = True
        while True:
            new_row = list(input("Введите строку матрицы: ").split())
            if len(new_row) != columns:
                print('Вводите правильное количество элементов в строке')
            else:

                for j in range(len(new_row)):
                    el = new_row[j]
                    if 'j' in el:
                        if el.index('j') == 0 or el.index('j') == 1:
                            first_part = el[:el.index('j') + 1]
                            second_part = el[el.index('j') + 1:]
                            if len(first_part) <= 2:
                                result = second_part + '+' + first_part
                            else:
                                result = second_part + first_part
                            try:
                                new_row[j] = complex(result)
                            except ValueError:
                                print("Вы неправильно ввели число!")
                                flag = False
                                break
                        else:
                            try:
                                new_row[j] = complex(el)
                            except ValueError:
                                print("Вы неправильно ввели число!")
                                flag = False
                                break
                    else:
                        try:
                            new_row[j] = float(el)
                        except ValueError:
                            print("Вы неправильно ввели число!")
                            flag = False
                            break
                if flag:
                    matrix.append(new_row)
                    break

    print()

    see_matrix(matrix)
    return matrix

def transponse_of_matrix_by_myself(matrix):
    """
    Функция, которая выводит транспонированную матрицу
    :params matrix: введенная матрица
    :return transposed: транспонированная матрица
    """
    transposed=[list(e) for e in zip(*matrix)]
    print()
    print('Транспонированная матрица')
    for i in range(len(transposed)):
        print(transposed[i])
    return transposed

def transponse_of_matrix_by_numpy(matrix):
    """
    Встроенная функция python, которая выводит транспонированную матрицу
    :params matrix: введенная матрица
    :return matrix_numpy: транспонированная матрица
    """
    matrix_numpy = np.array(matrix)
    return matrix_numpy

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

class Matrix:

    def __init__(self, matrix):
        """
        Функция, которая задает первую матрицу
        :params matrix: первая матрица
        """
        self.matrix = matrix

    def __add__(self, new_matrix):
        """
        Функция, которая позволяет складывать матрицы
        :params new_matrix: вторая матрица
        :return Matrix(result): результат сложения
        """
        m = len(self.matrix)
        n = len(self.matrix[0])
        if m == len(new_matrix.matrix) and n == len(new_matrix.matrix[0]):
            result = []
            for i in range(m):
                new_row = []
                for j in range(n):
                    new_row.append(self.matrix[i][j] + new_matrix.matrix[i][j])
                result.append(new_row)
            return Matrix(result)
        else:
            print("Ошибка! Введите соразмерные матрицы")

    def __sub__(self, new_matrix):
        """
        Функция, которая позволяет вычитать матрицы
        :params new_matrix: вторая матрица
        :return Matrix(result): результат вычитания
        """
        m = len(self.matrix)
        n = len(self.matrix[0])
        if m == len(new_matrix.matrix) and n == len(new_matrix.matrix[0]):
            result = []
            for i in range(m):
                new_row = []
                for j in range(n):
                    new_row.append(self.matrix[i][j] - new_matrix.matrix[i][j])
                result.append(new_row)
            return Matrix(result)
        else:
            print("Ошибка! Введите соразмерные матрицы")

    def __mul__(self, new_obj):
        """
        Функция, которая позволяет умножать матрицы
        :params new_obj: число/матрица
        :return Matrix(result): результат умножения
        """
        if isinstance(new_obj, (int, float, complex)):
            result = []
            for i in range(len(self.matrix)):
                new_row = []
                for j in range(len(self.matrix[0])):
                    new_row.append(self.matrix[i][j] * new_obj)
                result.append(new_row)
            return Matrix(result)

        elif isinstance(new_obj.matrix, list):
            rows_A = len(self.matrix)
            cols_A = len(self.matrix[0])
            rows_B = len(new_obj.matrix)
            cols_B = len(new_obj.matrix[0])
            if cols_A == rows_B:
                result = [[0 for row in range(cols_B)] for col in range(rows_A)]
                for i in range(rows_A):
                    for j in range(cols_B):
                        for k in range(cols_A):
                            result[i][j] += self.matrix[i][k] * new_obj.matrix[k][j]
                return Matrix(result)
            else:
                print("Ошибка! Нельзя умножить матрицы")
        else:
            print("Матрицу можно умножить на сормазмерную матрицу/число")

    def __str__(self):
        """
        Функция, которая выводит результат
        :return result: результат произведенных операций
        """
        result = ''
        for row in self.matrix:
            result += ' '.join(map(str, row)) + '\n'
        return result



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

def opr_sg_m():
    """
    Функция, которая считает определитель сгенерированной матрицы
    :params a: сгенерированная матрица
    :return det(matrix): определитель сгенерированной матрицы
    """
    matrix = generator_of_matrix()
    print('Сгенерированная матрица')
    for i in range(len(matrix)):
      print(matrix[i])
    print('Определитель сгенерированной матрицы равен')
    return det(matrix)
