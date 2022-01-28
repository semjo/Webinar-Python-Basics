"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
и возвращает сумму наибольших двух аргументов.
"""


def my_func(summand_1, summand_2, summand_3):
    summands = [summand_1, summand_2, summand_3]
    summands.sort(reverse=True)
    return sum(summands[:2])


print(my_func(13213, 234, 234411))
