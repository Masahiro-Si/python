# 4) Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым
# для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

# 5) Продолжить работу над первым заданием. Разработать методы, отвечающие
# за приём оргтехники на склад и передачу в определенное подразделение
# компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру,
# например словарь.

# 6) Продолжить работу над вторым заданием. Реализуйте механизм валидации
# вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.

class Storage:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        self._dict[equipment.model] = equipment

    def extract(self, equipment):
        return self._dict.items()


class OfficeEquipment:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price
        self._quantity = quantity
        self._group = self.__class__.__name__

    def group_name(self):
        return f'{self._group}'

    def __str__(self):
        return f'Марка: {self._name}, цена: {self._price},' \
               f' количество: {self._quantity}'


class Printer(OfficeEquipment):
    def __init__(self, model, name, price, quantity):
        super().__init__(name, price, quantity)
        self.model = model

    def __str__(self):
        return f'Тип: {self.__class__.__name__}, марка: {self._name},' \
               f' модель: {self.model}, цена: {self._price},' \
               f' количество: {self._quantity}'

    def unique(self):
        return f'Модель принтера: {self.model}.'


class Scanner(OfficeEquipment):
    def __init__(self, model, name, price, quantity):
        super().__init__(name, price, quantity)
        self.model = model

    def unique(self):
        return f'Модель сканера: {self.model}.'

    def __str__(self):
        return f'Тип: {self.__class__.__name__}, марка: {self._name},' \
               f' модель: {self.model}, цена: {self._price},' \
               f' количество: {self._quantity}'


class Xerox(OfficeEquipment):
    def __init__(self, name, price, quantity, model):
        super().__init__(name, price, quantity)
        self.model = model

    def unique(self):
        return f'Модель ксерокса: {self.model}.'

    def __str__(self):
        return f'Тип: {self.__class__.__name__}, марка: {self._name},' \
               f' модель: {self.model}, цена: {self._price},' \
               f' количество: {self._quantity}'


if __name__ == '__main__':
    storage = Storage()
    printer_1 = Printer('LJ100', 'HP', 12500, 14)
    print(printer_1)
    storage.add_to(printer_1)

    printer_2 = Printer('GB2200', 'Samsung', 33000, 25)
    print(printer_2)
    storage.add_to(printer_2)

    scanner_1 = Scanner('PTR098', 'Huawei', 20000, 10)
    scanner_2 = Scanner('HOPA', 'RusBus', 5000, 2)
    storage.add_to(scanner_1)
    storage.add_to(scanner_1)

    xerox_1 = Xerox('UMAO', 'Xiaomi', 90129, 90)
    storage.add_to(xerox_1)
    print(xerox_1)
