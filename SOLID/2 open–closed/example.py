from abc import ABC, abstractmethod
from enum import Enum


class Color(Enum):
    """Определение перечислений для цветов"""
    ORANGE = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    """Определение перечислений для размеров"""
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

    def __str__(self):
        return f"{self.name}"
        
class Specification(ABC):
    @abstractmethod
    def is_satisfies(self, item):
        """
        Абстрактный метод, который должен быть реализован в подклассах.
        Проверяет, удовлетворяет ли переданный объект заданному условию.
        """
        pass
    
class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfies(self, item):
        """
        Проверяет, соответствует ли цвет продукта заданному цвету.
        """
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfies(self, item):
        """
        Проверяет, соответствует ли размер продукта заданному размеру.
        """
        return item.size == self.size


class MultipleFieldSpecification(Specification):
    def __init__(self, *specs):
        """
        Принимает несколько спецификаций и объединяет их
        """
        self.specs: tuple[Specification] = specs # кортеж спецификаций

    def is_satisfies(self, item):
        """
        Проверяет, удовлетворяет ли продукт всем заданным условиям.
        Если хотя бы одно условие не выполнено, возвращается False.
        """
        for spec in self.specs:
            if not spec.is_satisfies(item):
                return False
        return True

class Filter(ABC):
    """Абстрактный класс Filter определяет интерфейс для фильтрации"""
    @abstractmethod
    def filter(self, items, spec: Specification):
        """
        Абстрактный метод для фильтрации списка по заданной спецификации.
        """
        pass

class ProductFilter(Filter):
    """Конкретная реализация фильтра для продуктов"""
    @staticmethod
    def filter(items, spec: Specification):
        """
        Фильтрует список продуктов, возвращая только те,
        которые удовлетворяют заданной спецификации.
        """
        for item in items:
            if spec.is_satisfies(item): # Проверяем, удовлетворяет ли продукт условию
                yield item # Возвращаем продукт как результат


products = [
    Product('apple', Color.GREEN, Size.SMALL),
    Product('grape', Color.GREEN, Size.MEDIUM),
    Product('avocado', Color.GREEN, Size.SMALL),
    Product('pumpkin', Color.ORANGE, Size.LARGE),
    Product('watermelon', Color.BLUE, Size.LARGE),
]


# Создание спецификаций для фильтрации:
color_spec = ColorSpecification(Color.GREEN)
size_spec = SizeSpecification(Size.SMALL)

# итемы, которые являются зелеными И маленькими
color_size_spec = MultipleFieldSpecification(color_spec, size_spec)

# Создание экземпляра фильтра
product_filter = ProductFilter()

# Применение фильтра к списку продуктов
for product in product_filter.filter(products, color_size_spec):
    print(product)
