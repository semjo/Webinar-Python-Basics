"""
4. Реализуйте базовый класс Car.
   у класса должны быть следующие атрибуты:
   speed, color, name, is_police (булево).
   А также методы: go, stop, turn(direction), которые должны сообщать,
   что машина поехала, остановилась, повернула (куда);
   опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
   добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
   для классов TownCar и WorkCar переопределите метод show_speed.
   При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
   Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
   Вызовите методы и покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.color} {self.name} поехала.")

    def stop(self):
        print(f"Машина {self.color} {self.name} остановилась.")

    def turn(self, direction):
        print(f"Машина {self.color} {self.name} повернула на {direction}.")

    def show_speed(self):
        print(f"Текущая скорость {self.color} {self.name} равна {self.speed}.")


class TownCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=False)

    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение скорости на {self.speed - 60} машиной {self.color} {self.name}!")


class SportCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=False)

    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение скорости на {self.speed - 40} машиной {self.color} {self.name}!")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=True)


taxi_car = TownCar(78, "black", "Mitsubishi")
taxi_car.go()
taxi_car.show_speed()
taxi_car.turn("право")
taxi_car.stop()

diablo_car = SportCar(120, "red", "Lamborghini")
diablo_car.go()
diablo_car.show_speed()
diablo_car.turn("лево")
diablo_car.stop()

tractor_car = WorkCar(43, "blue", "Belarus")
tractor_car.go()
tractor_car.show_speed()
tractor_car.turn("лево")
tractor_car.stop()

town_police_car = PoliceCar(60, "white", "Ford")
town_police_car.go()
town_police_car.show_speed()
town_police_car.turn("право")
town_police_car.stop()
