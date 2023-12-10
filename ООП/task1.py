# TODO Написать 3 класса с документацией и аннотацией типов
import math
import doctest

def check_variables(other_x, other_y, type):
    if (not isinstance(other_x, type)) or (not isinstance(other_y, type)):
        raise TypeError(f"Входные переменны должны быть типа {type}!")

class Dot:
    def __init__(self, other_x, other_y):
        """
         Создание и подготовка к работе объекта "Точка"

               :param other_x: Координата X точки
               :param other_y: Координата Y точки

               Примеры:
               >>> dot = Dot(25.0, 0.0)  # инициализация экземпляра класса
        """
        check_variables(other_x, other_y, (int, float))
        self.m_x = other_x
        self.m_y = other_y
    def move (self, delta_x=0, delta_y=0):
        """
        Функция изменяет координаты точки на определенное приращение

        :param delta_x: Приращение по X
        :param delta_y: Приращение по Y

        Примеры:
        >>> dot = Dot(25.0, 25.0)
        >>> dot.move(5.0,5.0)
        """
        check_variables(delta_x, delta_y, (int, float))
        self.m_x += delta_x
        self.m_y = delta_y
    def set_in_null (self):
        """
        Функция устанавливает координаты точки в 0

        Примеры:
        >>> dot = Dot(25.0, 25.0)
        >>> dot.set_in_null()
        """
        self.m_x = 0
        self.m_y = 0
class Rect:
    def __init__(self, other_LT, other_RB):
        """
         Создание и подготовка к работе объекта "Прямоугольник"

               :param other_LT: Координаты верхней левой точки прямоугольника
               :param other_RB: Координаты правой нижней точки прямоугольника

               Примеры:
               >>> dot_LT = Dot(2.0, 5.0)
               >>> dot_RB = Dot(6.0, 1.0)
               >>> rect = Rect(dot_LT, dot_RB)# инициализация экземпляра класса
        """
        check_variables(other_LT, other_RB, Dot)
        if (other_LT.m_x > other_RB.m_x) or (other_LT.m_y < other_RB.m_y):
            raise ValueError("Неправильный порядок операндов!")
        self.m_LT = other_LT
        self.m_RB = other_RB
    def inflate(self, i_x1,i_y1, i_x2, i_y2):
        """
            Функция изменяет координаты точек прямоугольника на определенное приращение

            :param i_x1: Приращение левой верхней по x
            :param i_y1: Приращение левой верхней по y
            :param i_x2: ППриращение правой нижней по x
            :param i_y2: Приращение правой нижней по y

            Примеры:
                >>> rect = Rect(Dot(2.0, 5.0), Dot(6.0, 1.0))
                >>> rect.inflate(1.0,1.0,1.0,1.0)
        """
        check_variables(i_x1, i_y1, (int, float))
        check_variables(i_x2, i_y1, (int, float))
        self.m_LT.m_x -= i_x1
        self.m_LT.m_y += i_y1
        self.m_RB.m_x += i_x2
        self.m_RB.m_y -= i_y2
    def square(self) -> float:
        """
            Функция вычисляет площадь прямоугольника
             :return: Площадь прямоугольника

            Примеры:
                >>> rect = Rect(Dot(2.0, 5.0), Dot(6.0, 1.0))
                >>> rect_square = rect.square()
        """
        return (self.m_RB.m_x - self.m_LT.m_x)*(self.m_LT.m_y - self.m_RB.m_y)

class Circle:
    def __init__(self, other_center, other_radius):
        """
         Создание и подготовка к работе объекта "Прямоугольник"

               :param other_center: Координаты центра окружности
               :param other_radius: Радиус окружности

               Примеры:
               >>> dot_LT = Dot(2.0, 5.0)
               >>> dot_RB = Dot(6.0, 1.0)
               >>> rect = Rect(dot_LT, dot_RB)# инициализация экземпляра класса
        """
        if not isinstance(other_center, Dot):
            raise TypeError(f"Центр круга должны быть типа Dot!")
        if not isinstance(other_radius, float):
            raise TypeError(f"Радиус должен быть типа float!")
        if other_radius < 0:
            raise ValueError(f"Радиус не может быть отрицательным")
        self.m_center = other_center
        self.m_radius = other_radius
    def inflate(self, delta):
        """
            Функция увеличивает радиус круга на определенное приращение

            :param delta: Приращение радиуса

            Примеры:
                >>> circle = Circle(Dot(2.0, 5.0),5.0)
                >>> circle.inflate(2.0)
        """
        self.m_radius +=delta
    def square(self) -> float:
        """
            Функция вычисляет площадь круга
             :return: Площадь круга

            Примеры:
                >>> circle = Circle(Dot(0.0,0.0), 5.0)
                >>> circle_square = circle.square()
         """
        return math.pi*self.m_radius**2





    if __name__ == "__main__":
        doctest.testmod()