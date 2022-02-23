"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий
   склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
   Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
   В базовом классе определите параметры, общие для приведённых типов.
   В классах-наследниках реализуйте параметры, уникальные для каждого типа
   оргтехники.
5. Разработайте методы, которые отвечают за приём оргтехники на склад
   и передачу в определённое подразделение компании. Для хранения данных
   о наименовании и количестве единиц оргтехники, а также других данных,
   можно использовать любую подходящую структуру (например, словарь).
6. Реализуйте механизм валидации вводимых пользователем данных.
   Например, для указания количества принтеров, отправленных на склад,
   нельзя использовать строковый тип данных.
"""


def validate(func):
    def existence(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError:
            print("На складе нет такого количества!")
        except KeyError:
            print("Нет такого материала!")

    return existence


class Warehouse:
    """   def __init__(self, cod_material, category_material, type_material, price, quantity=0):
           self.cod_material = cod_material
           self.category_material = category_material
           self.type_material = type_material
           self.price = price
           self.quantity = quantity
   """
    material_dict = {}

    @classmethod
    @validate
    def to_warehouse(cls, type_material, name_material, model_material, count_material):
        cls.material_dict[type_material][name_material][model_material]["count"] += count_material

    @classmethod
    @validate
    def from_warehouse(cls, type_material, name_material, model_material, count_material):
        count = cls.material_dict[type_material][name_material][model_material]["count"]
        if count < count_material:
            raise ValueError
        else:
            cls.material_dict[type_material][name_material][model_material]["count"] -= count_material

    @staticmethod
    def info_warehouse(key):
        print(Warehouse.material_dict[key])


class OfficeEquipment:

    def __init__(self, name_material, model_material, type_material, count_material=0):
        self.name_material = name_material
        self.model_material = model_material
        self.type_material = type_material
        try:
            if type(count_material) not in [int, float]:
                self.__count_material = 0
                raise ValueError
        except ValueError:
            print("Некорректный ввод данных!")
        else:
            self.__count_material = count_material
        finally:
            self.update_warehouse()

    def update_warehouse(self):
        warehouse_material = Warehouse.material_dict.get(self.type_material, {})
        if self.name_material in warehouse_material.keys():
            warehouse_material_name = warehouse_material[self.name_material]
            if self.model_material in warehouse_material.keys():
                warehouse_material_model = warehouse_material_name[self.model_material]
                warehouse_material_model["count"] += self.__count_material
            else:
                warehouse_material_name[self.model_material] = {"count": self.__count_material}
        else:
            warehouse_material[self.name_material] = {
                self.model_material: {"count": self.__count_material}
            }

        Warehouse.material_dict[self.type_material] = warehouse_material


class Printer(OfficeEquipment):
    def __init__(self, name_material, model_material, count_material, type_printer):
        super().__init__(name_material, model_material, "Принтер", count_material)
        self.type_printer = type_printer


class Scanner(OfficeEquipment):
    def __init__(self, name_material, model_material, count_material, type_scanner):
        super().__init__(name_material, model_material, "Сканер", count_material)
        self.type_scanner = type_scanner


class Copier(OfficeEquipment):
    def __init__(self, name_material, model_material, count_material, type_copier):
        super().__init__(name_material, model_material, "Ксерокс", count_material)
        self.type_copier = type_copier


printer_1 = Printer("Canon", "C2021", 10, "wifi")
scanner_1 = Scanner("HP", "w23", 5, "wifi")
copier_1 = Copier("Xerox", "wr453", 7, "wifi")
Warehouse.to_warehouse(type_material="Принтер", name_material="Xerox", model_material="sd45sdf", count_material=10)
Warehouse.to_warehouse(type_material="Принтер", name_material="Canon", model_material="C2021", count_material=3)
Warehouse.info_warehouse("Принтер")
Warehouse.from_warehouse(type_material="Принтер", name_material="Canon", model_material="C2021", count_material=5)
Warehouse.info_warehouse("Принтер")
Warehouse.from_warehouse(type_material="Принтер", name_material="Canon", model_material="C2021", count_material=15)
scanner_2 = Scanner("Canon", "w242", 8, "wifi")
Warehouse.info_warehouse("Принтер")
Warehouse.info_warehouse("Сканер")
Warehouse.info_warehouse("Ксерокс")
