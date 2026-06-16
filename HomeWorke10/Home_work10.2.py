# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.


from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self) -> float:
        pass
    @abstractmethod
    def get_perimeter(self) -> float:
        pass


class Triangle(Shape):

    def __init__(self, side: float) -> None:
        self.__side = side

    def get_area(self) -> float:
        return (math.sqrt(3) / 4) * self.__side ** 2

    def get_perimeter(self) -> float:
        return 3 * self.__side


    def __str__(self) -> str:
        return f"Рівносторонній трикутник (сторона={self.__side})"

class Rectangle(Shape):

    def __init__(self, a: float, b: float,):
        self.a = a
        self.b = b

    def get_area(self) -> float:
        return self.a * self.b

    def get_perimeter(self) -> float:
        return 2 * (self.a + self.b)

    def __str__(self) -> str:
        return f"Прямокутник (ширина={self.a}, висота={self.b})"

class Square(Shape):

    def __init__(self, a: float):
        self.a = a

    def get_area(self) -> float:
        return self.a * self.a

    def get_perimeter(self) -> float:
        return 4 * self.a

    def __str__(self) -> str:
        return f"Квадрат (сторона={self.a})"

if __name__ == '__main__':

    shapes = [ Triangle(5), Rectangle(4,9), Square(10)]

for shape in shapes:
    print(f"{shape}")
    print(f"{shape.get_area()}")
    print(f"{shape.get_perimeter()}")



