"""
3. Реализовать программу работы с органическими клетками, состоящими из ячеек.
   Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
   соответствующий количеству ячеек клетки (целое число).
   В классе должны быть реализованы методы перегрузки арифметических операторов:
   сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
   Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
   и целочисленное (с округлением до целого) деление клеток, соответственно.

   Сложение. Объединение двух клеток.
   При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
   Вычитание. Участвуют две клетки.
   Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
   иначе выводить соответствующее сообщение.
   Умножение. Создаётся общая клетка из двух.
   Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
   Деление. Создаётся общая клетка из двух.
   Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

   В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
   Данный метод позволяет организовать ячейки по рядам.
   Метод должен возвращать строку вида *****\n*****\n*****...,
   где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает,
   то в последний ряд записываются все оставшиеся.
   Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
   Тогда метод make_order() вернёт строку: *****\n*****\n**.
   Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
   Тогда метод make_order() вернёт строку: *****\n*****\n*****.
   Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""


class Cell:
    def __init__(self, number_cells):
        self.number_cells = number_cells

    def __add__(self, other):
        return Cell(self.number_cells + other.number_cells)

    def __sub__(self, other):
        if self.number_cells > other.number_cells:
            return Cell(self.number_cells - other.number_cells)
        else:
            print("В исходной клетке не достаточно ячеек!")

    def __mul__(self, other):
        return Cell(self.number_cells * other.number_cells)

    def __truediv__(self, other):
        return Cell(self.number_cells // other.number_cells)

    def make_order(self, number_row):
        return (("*" * number_row) + "\n") * (self.number_cells // number_row) + \
               "*" * (self.number_cells % number_row)


organic_cell_1 = Cell(6)
organic_cell_2 = Cell(3)
size_print = 5

organic_cell_3 = organic_cell_1 + organic_cell_2
print(f"Результатом сложения клетки:\n{organic_cell_1.make_order(size_print)}\n"
      f"и клетки:\n{organic_cell_2.make_order(size_print)}\n"
      f"является клетка: \n{organic_cell_3.make_order(size_print)}")

organic_cell_3 = organic_cell_1 - organic_cell_2
print(f"Результатом вычитания клетки:\n{organic_cell_1.make_order(size_print)}\n"
      f"и клетки:\n{organic_cell_2.make_order(size_print)}\n"
      f"является клетка: \n{organic_cell_3.make_order(size_print)}")

organic_cell_3 = organic_cell_1 * organic_cell_2
print(f"Результатом умножения клетки:\n{organic_cell_1.make_order(size_print)}\n"
      f"и клетки:\n{organic_cell_2.make_order(size_print)}\n"
      f"является клетка: \n{organic_cell_3.make_order(size_print)}")

organic_cell_3 = organic_cell_1 / organic_cell_2
print(f"Результатом деления клетки:\n{organic_cell_1.make_order(size_print)}\n"
      f"и клетки:\n{organic_cell_2.make_order(size_print)}\n"
      f"является клетка: \n{organic_cell_3.make_order(size_print)}")
