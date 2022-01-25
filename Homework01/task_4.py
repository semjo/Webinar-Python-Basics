"""
4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
num_user = input("Введите целое положительное число: ")
num_len = len(num_user)
max_figure = int(num_user[0])
i = 1
while i < num_len:
    if max_figure - int(num_user[i]) < 0:
        max_figure = int(num_user[i])
    i += 1
print("Самое большое число является: " + str(max_figure))
