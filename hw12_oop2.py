# =============================
# Домашняя работа: ООП на Python
# TeachMeSkills.by
# =============================

# Задание 1. Класс «Товар» и «Склад».
#
# Класс «Товар» содержит закрытые поля:
# - название товара
# - название магазина
# - стоимость в рублях
#
# Класс «Склад» содержит массив товаров.
#
# Обеспечить возможности:
# ✅ Вывод информации о товаре со склада по индексу
# ✅ Вывод информации о товаре со склада по имени
# ✅ Сортировка товаров по названию, по магазину и по цене
# ✅ Перегрузка сложения товаров по цене


# === TODO: реализовать класс Product ===
class Product:
    def __init__(self, name, shop, price):
        self.__name = name
        self.__shop = shop
        self.__price = price

    def __str__(self):
        return f"Товар: {self.__name}, в магазине: {self.__shop}, по цене: {self.__price} руб."

    def __add__(self, other):
        return self.__price + other.__price


    def get_name(self):
        return self.__name
        
    def get_shop(self):
        return self.__shop
        
    def get_price(self):
        return self.__price

# === TODO: реализовать класс Warehouse ===
class Warehouse:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        self.__products.append(product)

    def get_by_index(self, index):
        if 0 <= index < len(self.__products):
            return str(self.__products[index])

    def get_by_name(self, name):
        for product in self.__products:
            if product.get_name() == name:
                return str(product)

    def sort_by_name(self):
        self.__products.sort(key=lambda x: x.get_name())

    def sort_by_shop(self):
        self.__products.sort(key=lambda x: x.get_shop())

    def sort_by_price(self):
        self.__products.sort(key=lambda x: x.get_price())


# === Тесты для задачи 1 ===
print("=== Задача 1: Склад ===")
w = Warehouse()
p1 = Product("Молоко", "Пятерочка", 70)
p2 = Product("Хлеб", "Магнит", 40)
p3 = Product("Сыр", "Пятерочка", 300)

w.add_product(p1)
w.add_product(p2)
w.add_product(p3)

print(w.get_by_index(1))
print(w.get_by_name("Сыр"))

print("Сумма цен:", p1 + p2) 
print("\nСортировка по имени:")
w.sort_by_name()
for i in range(len(w._Warehouse__products)):
    print(w.get_by_index(i))

print("\nСортировка по магазину:")
w.sort_by_shop()
for i in range(len(w._Warehouse__products)):
    print(w.get_by_index(i))

print("\nСортировка по цене:")
w.sort_by_price()
for i in range(len(w._Warehouse__products)):
    print(w.get_by_index(i))

# =============================
# Задание 2. Класс «ПчёлоСлон».
#
# Инициализируется двумя числами:
# - часть пчелы
# - часть слона
#
# Методы:
# ✅ Fly() – True, если часть пчелы >= части слона
# ✅ Trumpet() – "tu-tu-doo-doo", если часть слона >= пчелы, иначе "wzzzz"
# ✅ Eat(meal, value) – meal только "nectar" или "grass".
#   - если nectar: у слона уменьшается, у пчелы увеличивается
#   - если grass: наоборот
#   - нельзя выйти за пределы 0–100


# === TODO: реализовать класс BeeElephant ===
class BeeElephant:
    def __init__(self, bee_part, elephant_part):
        self.__bee = max(0, min(100, bee_part))
        self.__elephant = max(0, min(100, elephant_part))
    
    def fly(self):
        return self.__bee >= self.__elephant


    def trumpet(self):
        if self.__elephant >= self.__bee:
            return "tu-tu-doo-doo"
        return "wzzzz"

    def eat(self, meal, value):
        if meal == "nectar":
            self.__bee = min(100, self.__bee + value)
            self.__elephant = max(0, self.__elephant - value)
        elif meal == "grass":
            self.__bee = max(0, self.__bee - value)
            self.__elephant = min(100, self.__elephant + value)
        total = self.__bee + self.__elephant
        if total > 100:
            scale = 100 / total
            self.__bee = self.__bee * scale
            self.__elephant = self.__elephant * scale


# === Тесты для задачи 2 ===
print("\n=== Задача 2: ПчёлоСлон ===")
be = BeeElephant(30, 70)
print(be.fly())            # False
print(be.trumpet())        # tu-tu-doo-doo
be.eat("nectar", 20)       # должно изменить пропорции
print(be.fly())            # возможно True


# =============================
# Задание 3. Класс «Автобус».
#
# Свойства:
# ✅ скорость
# ✅ макс. кол-во мест
# ✅ макс. скорость
# ✅ список фамилий пассажиров
# ✅ флаг наличия свободных мест
# ✅ словарь мест (номер: фамилия)
#
# Методы:
# ✅ посадка/высадка одного или нескольких пассажиров
# ✅ увеличение/уменьшение скорости на заданное значение
# ✅ операции:
#   - `in` проверяет фамилию в списке
#   - `+=` посадка
#   - `-=` высадка


# === TODO: реализовать класс Bus ===
class Bus:
    def __init__(self, max_seats, max_speed):
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.speed = 0
        self.seats = {}
        for seat_number in range(1, max_seats + 1):
            self.seats[seat_number] = None
    
    def passengers_list(self):
        return [surname for surname in self.seats.values() if surname is not None]

    def free_seats(self):
        return None in self.seats.values()

    def board(self, *passengers):
        for surname in passengers:
            if not self.free_seats():
                break
            for seat_number, occupant in self.seats.items():
                if occupant is None:
                    self.seats[seat_number] = surname
                    break

    def unboard(self, *passengers):
        for surname in passengers:
            for seat_number, occupant in self.seats.items():
                if occupant == surname:
                    self.seats[seat_number] = None

    def change_speed(self, delta):
        new_speed = self.speed + delta
        self.speed = max(0, min(self.max_speed, new_speed))

    def __contains__(self, surname):
        return surname in self.passengers_list()

    def __iadd__(self, surname):
        self.board(surname)
        return self

    def __isub__(self, surname):
        self.unboard(surname)
        return self


# === Тесты для задачи 3 ===
print("\n=== Задача 3: Автобус ===")
bus = Bus(max_seats=3, max_speed=100)
bus.board("Иванов", "Петров")
print("Иванов" in bus)     # True
bus += "Сидоров"
print("Сидоров" in bus)    # True
bus -= "Петров"
print("Петров" in bus)     # False
bus.change_speed(20)