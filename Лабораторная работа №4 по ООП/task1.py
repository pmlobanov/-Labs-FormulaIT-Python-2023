import doctest
# базовый класс
class Automobile:
    """
    Класс, абстрагирующий абстактный автомобиль, хранит в себе марку машины, длину и вес
    """
    @staticmethod
    def _check_input(value: int) -> None:
        """
        Проверка целого числа на подходимость для использования в классе. Размеры не должны быть отрицательны
        Является внутренним служебным методом, поэтому недоступен изнве.
        Метод унаследован дочерними классами, в силу добавления новых физических свойств и необходимости их проверки
            :param value: проверяемое значение
        """
        if value <= 0:
            raise TypeError("Переменная не может быть отрицательной!")
    # атрибуты класса недоступны извне так как по логике не могут быть изменены после создания экзепляра класса
    # являются protected, для доступности при наследовании
    def __init__(self, brand: str, length: int, weight: int) -> None:
        """
        Создание и  подготовка к работе обьекта "Автомобиль".
        Для каждой целочисленной переменной проводится проверка ее подходимость (положительное значение)
            :param brand: марка автомобиля
            :param length: длина автомобиля в миллиметрах
            :param weight: вес конструкции автомабиля в килограммах

            Примеры:
            >>> Auto1 = Automobile("Toyota", 4388, 1555)
        """
        for i in locals():
            if isinstance(i, int):
                self._check_input(i)
        self._brand = brand
        self._length = length
        self._weight = weight

    def __str__(self) -> str:
        """
              Представляет "удобоворимый" текстовый образ обькекта "Автомобиль" понятный для чтения человеком

              Пример:
              >>> Auto1 = Automobile("Toyota", 4388, 1555)
              >>> autostring = Auto1
        """
        return f"Марка {self._brand}, Длина {self._length}, Вес {self._weight}"


    def __repr__(self) -> str:
        """
        Представляет "официальный" текстовый образ обькекта "Автомобиль"

        Пример:
        >>> Auto1 = Automobile("Toyota", 4388, 1555)
        >>> Auto2 =repr(Auto1)
        """
        return f"{self.__class__.__name__}(brand={self._brand!r}, length={self._length}, weight={self._weight})"

    def can_cary_that_weight(self, weight) -> None:
        """
        Метод проверяющий, может ли автомобиль ту нагрузку, которую мы хотим в него положить
        Абстрактный автомобиль не может ничего везти, поэтому метод = заглушка.

        """
        return None
# дочерний класс №1
class Car(Automobile):
    """
    Класс "Легковой автомобиль" хранит в себе марку машины, ее модель, длину, вес, и количество вмещающихся человек
    """
    # атрибуты класса недоступны извне так как по логике не могут быть изменены после создания экзепляра класса
    # являются protected, для доступности при наследовании
    def __init__(self, brand: str,model: str, length: int, weight: int, human_capacity: int) -> None:
        """
               Создание и  подготовка к работе обьекта "Легковой автомобиль".
               Для унаследованной части вызывается конструктор базового класса
               Для каждой целочисленной переменной проводится проверка ее подходимость (положительное значение)
                   :param brand: марка автомобиля
                   :param length: длина автомобиля в миллиметрах
                   :param weight: вес конструкции автомабиля в килограммах
                   :param model: модель автомобиля
                   :param human_capacity: вес конструкции автомабиля в килограммах


                   Примеры:
                   >>> car1 = Car("Ford", "Focus", 4693 , 1060, 5)
               """
        super().__init__(brand, length, weight)
        self._check_input(human_capacity)
        self._model = model
        self._human_capacity = human_capacity

    def __repr__(self) -> str:
        """
           Представляет "официальный" текстовый образ обькекта "Легковой автомобиль"

           Пример:
           >>> car1 = Car("Ford", "Focus", 4693 , 1060, 5)
           >>> car2 = repr(car1)
           """
        return f"{self.__class__.__name__}(brand={self._brand!r}, model={self._model!r}, length={self._length}" \
               f", weight={self._weight}, human_capacity= {self._human_capacity} )"

    def can_cary_that_weight(self, weight) -> bool:
        """
             Метод проверяющий, может ли автомобиль ту нагрузку, которую мы хотим в него положить
             Так как класс хранит лишь количество посадочных мест, то с помощью среднего веса человека можно
             примерно вычислить какой вес может выдержать машина

                :param weight: вес, который мы хотим поместить в машину

                Пример
                >>> car1 = Car("Ford", "Focus", 4693 , 1060, 5)
                >>> bool1 = car1.can_cary_that_weight(500)
             """
        if ((weight / 78) > self._human_capacity):
            return False
        return True

# дочерний класс №2

class Truck(Automobile):
    # атрибуты класса недоступны извне так как по логике не могут быть изменены после создания экзепляра класса
    # являются protected, для доступности при наследовании
    def __init__(self, brand: str, model: str, length: int, weight: int, payload: int) -> None:
        """
         Создание и  подготовка к работе обьекта "Легковой автомобиль".
         Для унаследованной части вызывается конструктор базового класса
         Для каждой целочисленной переменной проводится проверка ее подходимость (положительное значение)
             :param brand: марка автомобиля
             :param length: длина автомобиля в миллиметрах
             :param weight: вес конструкции автомабиля в килограммах
             :param model: модель автомобиля
             :param payload: полезная нагрузка автомобиля


             Примеры:
             >>> truck1 = Truck("ГАЗ", "3307" , 6550 , 3350, 4500)
         """
        super().__init__(brand, length, weight)
        self._check_input(payload)
        self._model = model
        self._payload = payload

    def __repr__(self) -> str:
        """
               Представляет "официальный" текстовый образ обькекта "Грузовой автомобиль"

               Пример:
               >>> truck1 = Truck("ГАЗ", "3307" , 6550 , 3350, 4500)
               >>> truck2 = repr(truck1)
               """
        return f"{self.__class__.__name__}(brand={self._brand!r}, model={self._model!r}, length={self._length}, " \
               f"weight={self._weight}, payload= {self._payload})"

    def can_cary_that_weight(self, weight) -> bool:
        """
           Метод проверяющий, может ли автомобиль ту нагрузку, которую мы хотим в него положить
              :param weight: вес, который мы хотим поместить в машину

              Пример
              >>> truck1 = Truck("ГАЗ", "3307" , 6550 , 3350, 4500)
              >>> bool1 =truck1.can_cary_that_weight(2500)
           """
        if weight > self._payload:
            return False
        return True




if __name__ == "__main__":
    doctest.testmod()
