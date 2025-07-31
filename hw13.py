# ================================
# TeachMeSkills.by — Домашнее задание
# ================================
"""
Здесь задания на генераторы и паттерны проектирования:
- Строитель
- Фабричный метод
- Стратегия

Заполняйте TODO, читайте комментарии и запускайте тесты.
"""

# ================================
# ЗАДАНИЕ 1: Генератор чисел Фибоначчи
# ================================

def fibonacci_generator(n: int):
    numbers = []
    a, b = 0, 1
    
    for i in range(n):
        numbers.append(a)
        a, b = b, a + b
    
    return numbers

# Тест:
print("\n--- Задание 1 ---")
n = int(input("Сколько чисел Фибоначчи вывести? "))
for num in fibonacci_generator(n):
    print(num, end=' ')
print()


# ================================
# ЗАДАНИЕ 2: Бесконечная циклическая последовательность
# ================================

def cycle_123():
    num_list = [1, 2, 3]
    index = 0
    while True:
        yield num_list[index]
        index += 1
        if index == len(num_list):
            index = 0
# Тест:
print("\n--- Задание 2 ---")
count = int(input("Сколько чисел вывести из бесконечного цикла? "))
gen = cycle_123()
for _ in range(count):
    print(next(gen), end=' ')
print()


# ================================
# ЗАДАНИЕ 3: Паттерн «Строитель»
# ================================

class Pizza:
    def __init__(self):
        self.size = None
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def __str__(self):
        return f"Pizza(size={self.size}, cheese={self.cheese}, pepperoni={self.pepperoni}, mushrooms={self.mushrooms}, onions={self.onions}, bacon={self.bacon})"


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def set_size(self, size):
        self.pizza.size = size
        return self

    def add_cheese(self):
        self.pizza.cheese = True
        return self
    
    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self
    
    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self
    
    def add_onions(self):
        self.pizza.onions = True
        return self
    
    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def build(self):
        completed_pizza = self.pizza
        self.pizza = Pizza()
        return completed_pizza


class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def make_pizza(self):
        return (self.builder
                .set_size(60)
                .add_cheese()
                .add_pepperoni()
                .add_bacon()
                .build())


# Тест:
print("\n--- Задание 3 ---")
builder = PizzaBuilder()
director = PizzaDirector(builder)
pizza = director.make_pizza()
print(pizza)


# ================================
# ЗАДАНИЕ 4: Паттерн «Фабричный метод»
# ================================

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Гав!"


class Cat(Animal):
    def speak(self):
        return "Мяу!"


class AnimalFactory:
    def create_animal(self, animal_type: str) -> Animal:
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError(f"Неизвестный тип животного: {animal_type}")


# Тест:
print("\n--- Задание 4 ---")
factory = AnimalFactory()
animal = factory.create_animal("dog")
print(animal.speak()) 
animal = factory.create_animal("cat")
print(animal.speak()) 


# ================================
# ЗАДАНИЕ 5: Паттерн «Стратегия»
# ================================

class OperationStrategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass


class Addition(OperationStrategy):
    def execute(self, a, b):
        return a + b


class Subtraction(OperationStrategy):
    def execute(self, a, b):
        return a - b


class Multiplication(OperationStrategy):
    def execute(self, a, b):
        return a * b


class Division(OperationStrategy):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("делить на ноль нельзя")
        return a / b


class Calculator:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy: OperationStrategy):
        self.strategy = strategy

    def calculate(self, a, b):
        return self.strategy.execute(a, b)


# Тест:
print("\n--- Задание 5 ---")
calc = Calculator()
calc.set_strategy(Addition())
print("5 + 3 =", calc.calculate(5, 3))
calc.set_strategy(Subtraction())
print("5 - 3 =", calc.calculate(5, 3))
calc.set_strategy(Multiplication())
print("5 * 3 =", calc.calculate(5, 3))
calc.set_strategy(Division())
print("5 / 3 =", calc.calculate(5, 3))


# ================================
# УДАЧИ! 🚀
# ================================