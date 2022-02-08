"""
2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
"""


def personal_data(**kwargs):
    return f"Имя: {kwargs['first_name']}, Фамилия: {kwargs['last_name']}, Год рождения: {kwargs['year_birth']}," \
           f" Город проживания: {kwargs['city_residence']}, Email: {kwargs['email']}, Телефон: {kwargs['tel']}"


print(personal_data(first_name="Edgard", last_name="Pupkin", year_birth=2000, city_residence="Moskow",
                    email="pyhton@mail.ru", tel="89925846751"))
