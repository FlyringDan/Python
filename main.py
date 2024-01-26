# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass


class Student:
    """
    Создание класса "Студент"

    :param name: Имя студента
    :param surname: Фамилия студента
    :param mark: Оценка студента

    Пример:
    >>> Daniil = Student("Daniil", "Bryk", 4) #Инициализация класса студент

    """
    def __init__(self, name: str, sur_name: str, mark: int):
        if not isinstance(name, (str)):
            raise TypeError("Name must be a string")
        if not isinstance(sur_name, (str)):
            raise TypeError("Surname Must be a string")
        if not isinstance(mark, (int)):
            raise TypeError("Mark must be an integer")
        self.name = name
        self.sur_name = sur_name
        self.mark = mark

    def get_mark(self) -> int:
        """
        Функция, которая вываодит оценку студента

        :return: Оценка студента
        Примеры:
        >>> Artem = Student("Романов", "Артём", 5)
        >>> Artem.get_mark
        5
        """
        return self.mark


    def get_name(self) -> str:
        """
        Функцция get_name выводит имя студента
        :return: Имя студента
        Пример:
        >>> Daniil = Student("Daniil", "Bryk", 4)
        >>> Daniil.get_name
        "Daniil"
        """

        return self.name


    def set_mark(self, new_mark: int) -> None:
        """
        Функция set_mark позволяет изменить оценку, выбранному студенту
        >>> Daniil = Student("Daniil", "Bryk", 4)
        >>> Daniil.set_mark(5)
        >>> Daniil.get_mark
        5
        """
        self.mark = new_mark


    def change_name(self, new_name: str) -> None:
        """
        Функция change_name поволяет изменить имя, выбранному студенту
        >>> Daniil = Student("Daniil", "Bryk", 4)
        >>> Daniil.change_name("Artem")
        >>> Daniil.get_name
        "Artem"
        """
        self.name = new_name


class Triangle:
    def __init__(self, a: float, b: float, c: float, h: float):
        """
        Создание класса "Треугольник"

        :param: a: сторона
        :param: b: сторона
        :param: c: сторона
        :paran: h: высота

        Пример:
        >>> Triangle = Triangle(4, 3, 5, 5)
        """
        self.a = a
        self.b = b
        self.c = c
        self.h = h


    def area(self, a: float, h: float) -> float:
        """
        Функция area позволяет вычислить площадь треугольника
        :return: Площадь
        Пример:
        >>> Triangle = Triangle(4,3,5,5)
        >>> Triangle.area()
        10
        """
        return a * h / 2


    def perimeter(self, a: float, b: float, c: float) -> float:
        """
        Функция perimeter позволяет вычислить периметр треугольника по трём его сторонам
        :return: Периметр
        Пример:
        >>> Triangle = Triangle(4,3,5,5)
        >>> Triangle.area()
        17
        """
        return a + b + c


class Alarm:
    def __init__(self, time_to_ring: int, remains_time: int, time_is_now: int):
        self.time_to_ring = time_to_ring
        self.time_is_now = time_is_now
        self.remains_time = time_to_ring - time_is_now
        """
        Класс будильник, у которого 3 характеристики: время звонка, оставшееся время до звонка и время в данный момент
        :param: time_to_ring
        :param: remains_time
        :param: time_is_now
        
        Пример:
        >>> Alarm = Alarm(1400, 2004)
        """


    def set_time_to_ring(self, new_time_to_ring: int) -> None:
        """
        Функция set_time_to_ring позволяет установить время звонка
        >>> Alarm = Alarm(1400, 2004)
        >>> Alarm.set_time_to_ring(1500)
        1500
        """
        self.time_to_ring = new_time_to_ring


    def get_remains_time(self) -> int:
        """
        Функция get_remains_time позволяет узнать оставшееся время до звонка
        Пример:
        >>> Alarm = Alarm(1400, 2000)
        >>> Alarm.get_remains_time()
        600
        """
        return self.remains_time