class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        self.check_pages(pages)
        super().__init__(name, author)
        self._pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"

    @staticmethod
    # проверка входящей величины
    def check_pages(new_pages):
        #проверка на тип
        if type(new_pages) != int: raise ValueError("Число страниц должно быть целым!")
        #проверка на допустимые значения
        if (new_pages <= 0): raise ValueError("Количество страниц в книге должно быть больше нуля!")
    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages):
        self.check_pages(new_pages)
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        self.check_duration(duration)
        super().__init__(name, author)
        self._duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._duration!r})"

    @staticmethod
    #проверка входящей величины
    def check_duration(new_duration):
        # проверка на тип
        if type(new_duration) != float: raise ValueError("Число страниц должно быть представленно десятичной дробью!")
        # проверка на допустимые значения
        if (new_duration <= 0): raise ValueError("Продолжительность аудиокниги должна быть положительным числом!")
    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration):
        self.check_duration(new_duration)
        self._duration = new_duration


