"""
6.  Сформировать (не программно) текстовый файл.
    В нём каждая строка должна описывать учебный предмет и наличие лекционных,
    практических и лабораторных занятий по предмету.
    Сюда должно входить и количество занятий.
    Необязательно, чтобы для каждого предмета были все типы занятий.
    Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
    Вывести его на экран.
"""
report_dict = {}
with open("Report", "r", encoding="utf-8") as report_text:
    for string in report_text:
        academic_subject, *str_subjects = string.split()
        int_subjects = [int(value.rstrip('(л)(пр)(лаб)')) for value in str_subjects if value != "-"]
        report_dict.update({academic_subject.rstrip(":"): sum(int_subjects)})

    print(report_dict)
