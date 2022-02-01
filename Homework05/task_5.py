"""
5.  Создать (программно) текстовый файл, записать в него программно набор чисел,
    разделённых пробелами.
    Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
with open("Numbers", "w") as file_num:
    numbers = input("Введите числа через пробел: ")
    print(numbers, file=file_num)

with open("Numbers") as file_num:
    string = file_num.read().rstrip().split()
