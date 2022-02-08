"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
   который должен принимать данные (список списков) для формирования матрицы.

   Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
   Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

   31    32         3    5    32        3    5    8    3
   37    43         2    4    6         8    3    7    1
   51    86        -1   64   -8

   Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
   Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
   класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
   Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
   складываем с первым элементом первой строки второй матрицы и т.д.
"""
import array


class Matrix:
    def __init__(self, array):
        self.array = array

    def __str__(self):
        array_str = ""
        for row in self.array:
            for elem in row:
                array_str += str(elem) + ' '
            array_str += '\n'
        return array_str

    def __add__(self, other):
        new_array = []
        for col in range(len(self.array)):
            add_row = []
            for row in range(len(self.array[col])):
                try:
                    add_row.append(self.array[col][row] + other.array[col][row])
                except IndexError:
                    print("Ошибка. У матриц не совпадают размерность.")
                    return
            new_array.append(add_row)
        return Matrix(new_array)


a_list = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
b_list = [[3, 2, 1], [3, 2, 1], [3, 2, 1]]
c_list = []
a_matrix = Matrix(a_list)
b_matrix = Matrix(b_list)
c_matrix = Matrix(c_list)
print(a_matrix)
print(b_matrix)
c_matrix = a_matrix + b_matrix
print(c_matrix)
