if __name__ == "__main__":

    class Car:
        def __init__(self, model: str, country: str):
            self.model = model
            self.country = country

        def __str__(self):
            return f"Модель машины: {self.model}, Страна машины: {self.country}"

        def __repr__(self):
            return f"{Car}(model={self.model}), country={self.country}"

        def change_country(self, new_country: str):
            self.country = new_country
            return self.country

    class LightCar(Car):
        def __init__(self, model: str, country: str, count_of_seats: int):
            super().__init__(model, country)
            self.count_of_seats = count_of_seats

        def __str__(self):
            return f"Количество людей в машине: {self.count_of_seats}"

        def __repr__(self):
            return f"{Car}(count_of_seats={self.count_of_seats})"

        def change_country(self, new_country: str):
            super().change_country(new_country)
            return self.country

    class HeavyCar(Car):
        def __init__(self, model: str, country: str, count_of_wheels: int):
            super().__init__(model, country)
            if (count_of_wheels / 2) == 0:
                self.count_of_wheels = count_of_wheels

        def __str__(self):
            return f"Количество колёс: {self.count_of_wheels}"

        def __repr__(self):
            return f"{Car}(count_of_seats={self.count_of_wheels})"

        def change_country(self, new_country: str):
            super().change_country(new_country)
            return self.country
    pass

