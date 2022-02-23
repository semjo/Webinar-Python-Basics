"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать
   дату в виде строки формата «день-месяц-год». В рамках класса реализовать
   два метода. Первый, с декоратором @classmethod. Он должен извлекать число,
   месяц, год и преобразовывать их тип к типу «Число». Второй,
   с декоратором @staticmethod, должен проводить валидацию числа,
   месяца и года (например, месяц — от 1 до 12).
   Проверить работу полученной структуры на реальных данных.
"""
from datetime import date


class DateCl:

    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def c_num(cls, date_str):
        try:
            day_date, month_date, year_date = [int(pos) for pos in date_str.split("-")]
            return day_date, month_date, year_date
        except ValueError:
            print("Не корректно введена дата!")

    @staticmethod
    def validate(day_date, month_date, year_date):
        try:
            date(year_date, month_date, day_date)
            return True
        except ValueError:
            print("Не корректно указана дата!")


date_val = DateCl("10-02-2002")
if DateCl.c_num(date_val.date_str):
    day_val, month_val, year_val = DateCl.c_num(date_val.date_str)
    if date_val.validate(day_val, month_val, year_val):
        print(f"День: {day_val}, Месяц: {month_val}, Год: {year_val}")
