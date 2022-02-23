"""
6. Реализовать два небольших скрипта:
итератор, генерирующий целые числа, начиная с указанного;
итератор, повторяющий элементы некоторого списка, определённого заранее.
Подсказка: используйте функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Предусмотрите условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3.
При достижении числа 10 — завершаем цикл.
Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.
"""
from itertools import count, cycle


def generate_int(begin, counts):
    for el in count(begin):
        if el > begin + counts:
            break
        yield el


num_begin = 2
num_count = 10
print(f"Генерация целых чисел начиная с {num_begin} и заканчивая {num_begin + num_count}:")
for val in generate_int(num_begin, num_count):
    print(val, end=" ")
print()


def generate_replay(rep_string, rep_num):
    i = 1
    for el in cycle(rep_string):
        if i > rep_num:
            break
        i += 1
        yield el


my_string = "GOOD"
rep = 8
print(f"Повторение элементов списка {my_string} {rep} раз:")
for val in generate_replay(my_string, rep):
    print(val, end=" ")
