"""
3.  Создать текстовый файл (не программно).
    Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
    Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
    Выполнить подсчёт средней величины дохода сотрудников.
"""
budget = 0
slice_salary = 20000
with open("Staff", encoding="utf-8") as file_staff:
    strings = file_staff.readlines()
    for string in strings:
        second_name, salary = string.split()
        if float(salary) < slice_salary:
            print(f"Сотрудник {second_name} имеет оклад менее {slice_salary}")
        budget += float(salary)
print("Cредняя величины дохода сотрудников: ", budget / len(strings))