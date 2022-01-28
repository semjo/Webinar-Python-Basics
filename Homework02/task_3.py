"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и dict.
"""
try:
    my_month = int(input("Введите месяц года: "))
except ValueError:
    print("Введено нецелочисленное значение.")
else:
    my_year = {
        'зима': (12, 1, 2),
        'весна': (3, 4, 5),
        'лето': (6, 7, 8),
        'осень': (9, 10, 11)}
    for val in my_year:
        if my_year[val].count(my_month):
            print(f"Месяц относится к времени года {val}")
            break
    else:
        print("Такого месяца нет.")
