"""
5. Реализовать класс Stationery (канцелярская принадлежность).
   определить в нём атрибут title (название) и метод draw (отрисовка).
   Метод выводит сообщение «Запуск отрисовки»;
   создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
   в каждом классе реализовать переопределение метода draw.
   Для каждого класса метод должен выводить уникальное сообщение;
   создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Выбрана", self.title)


class Pencil(Stationery):
    def draw(self):
        print("Выбран", self.title)


class Handle(Stationery):
    def draw(self):
        print("Выбран перманентный", self.title)


my_pen = Pen("ручка")
my_pen.draw()
my_pencil = Pencil("карандаш")
my_pencil.draw()
my_handle = Handle("маркер")
my_handle.draw()
