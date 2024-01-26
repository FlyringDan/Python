class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def get_pages(self):
        return self.pages

    def set_pages(self, number_of_pages: int):
        if number_of_pages > 0:
            self.pages = number_of_pages
        else:
            raise ValueError("Number of pages must be more than zero")

    def __str__(self):
        return f"Book {self.name}, Author {self.author}, Pages {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name = {self.name!r}, author = {self.author!r}, pages = {self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def get_duration(self):
        return self.duration

    def set_duration(self, number_of_duration: float):
        if number_of_duration > 0:
            self.duration = number_of_duration
        else:
            ValueError("Number of duration must be more then zero")

    def __str__(self):
        return f"Book {self.name}, Author {self.author}, Pages {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name = {self.name!r}, author = {self.author!r}, duration = {self.duration!r})"


