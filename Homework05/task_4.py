"""
4.  Создать (не программно) текстовый файл со следующим содержимым:
    One — 1
    Two — 2
    Three — 3
    Four — 4
    Напишите программу, открывающую файл на чтение и считывающую построчно данные.
    При этом английские числительные должны заменяться на русские.
    Новый блок строк должен записываться в новый текстовый файл.
"""

russ_dictinary = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("Numeric", encoding="utf-8") as file_eng, open("Numeric_rus", "w", encoding="utf-8") as file_rus:
    for string in file_eng.readlines():
        num_string, number = string.rstrip().split(" - ")
        file_rus.write(f"{russ_dictinary[num_string]} - {number}\n")
