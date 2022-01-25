"""
5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделённых пробелом и снова нажать Enter.
Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введён после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""


def my_sum(summands):
    summands = summands.split()
    summ = 0
    for summand in summands:
        if summand:
            try:
                if summand == "q":
                    return summ, False
                else:
                    summ += int(summand)
            except ValueError:
                continue
    return summ, True


summ = 0
stop = True
while stop:
    interim_amounts, stop = my_sum(input("Введите числа через пробел. Чтобы остановить ввод введите q: "))
    summ += interim_amounts
print(f"Результат суммирования: {summ}")
