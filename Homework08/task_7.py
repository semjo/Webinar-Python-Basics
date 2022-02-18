"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс
   «Комплексное число». Реализуйте перегрузку методов сложения и умножения
   комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры
   класса (комплексные числа), выполните сложение и умножение созданных
   экземпляров. Проверьте корректность полученного результата.
"""


class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary,
                       self.real * other.imaginary + self.imaginary * other.real)

    def __str__(self):
        return f"{self.real} + {self.imaginary}j"


complex_1 = Complex(3, 2)
complex_2 = Complex(1, 7)
print(f"({complex_1}) + ({complex_2}) = {complex_1 + complex_2}")
print(f"({complex_1}) * ({complex_2}) = {complex_1 * complex_2}")
