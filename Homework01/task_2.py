"""
2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
sec = int(input("Введите время в секундах: "))

print(f'введенное время составило: {(sec // 3600):02d}:'
      f'{(sec % 3600 // 60):02d}:'
      f'{(sec % 3600 % 60):02d}')
