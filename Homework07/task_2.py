"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
   Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
   К типам одежды в этом проекте относятся пальто и костюм.
   У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
   Это могут быть обычные числа: V и H, соответственно.
   Для определения расхода ткани по каждому типу одежды использовать формулы:
   для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
   Реализовать общий подсчет расхода ткани.
   Проверить на практике полученные на этом уроке знания:
   реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size):
        self.size = size

    @abstractmethod
    def fabric_consumption(self):
        pass


class Coat(Clothes):

    def __str__(self):
        return "пальто c размером " + str(self.size)

    @property
    def fabric_consumption(self):
        return round(self.size / 6.5 + 0.5, 3)


class Suit(Clothes):
    def __str__(self):
        return "костюм c ростовкой " + str(self.size)

    @property
    def fabric_consumption(self):
        return round(self.size * 2 + 0.3, 3)


my_coat = Coat(52)
my_suit = Suit(1.84)
print(f"На {my_coat} необходимо {my_coat.fabric_consumption} ткани")
print(f"На {my_suit} необходимо {my_suit.fabric_consumption} ткани")
cloth = my_coat.fabric_consumption + my_suit.fabric_consumption
print(f"Для выбранной одежды необходимо {cloth} ткани")
