"""
7. Создать вручную и заполнить несколькими строками текстовый файл,
   в котором каждая строка будет содержать данные о фирме:
   название, форма собственности, выручка, издержки.

   Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
   а также среднюю прибыль.
   Если фирма получила убытки, в расчёт средней прибыли её не включать.

   Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
   а также словарь со средней прибылью.
   Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

   Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 3000}]
Подсказка: использовать менеджер контекста.
"""
import json

firms_profits_list = []
with open("Firms", encoding="utf-8") as firms_file:
    firms_sum_profit_for_average = []
    firms_profits_dict = {}
    for string in firms_file.readlines():
        firm_name, _, firm_revenue, firm_cost = string.rstrip().split()
        firm_profit = int(firm_revenue) - int(firm_cost)
        firms_profits_dict[firm_name] = firm_profit
        if firm_profit > 0:
            firms_sum_profit_for_average.append(firm_profit)
    firms_profits_list.append(firms_profits_dict)
    firms_profits_list.append({"average_profit": sum(firms_sum_profit_for_average) / len(firms_sum_profit_for_average)})

with open("Firms.json", "w") as firms_file:
    json.dump(firms_profits_list, firms_file)
