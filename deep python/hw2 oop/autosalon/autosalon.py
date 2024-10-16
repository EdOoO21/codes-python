class StringValue:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __set_name__(self, owner, name):
        self.name = "_" + name  # Обратите внимание, имя должно быть protected

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if (type(value) is str) and (
                self.max_length >= len(value) >= self.min_length):
            setattr(instance, self.name, value)


class PriceValue:
    def __init__(self, max_value):
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = "_" + name
        # Обратите внимание, имя должно быть protected

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if ((type(value) is int) or (type(value) is float)) and (
                self.max_value >= value >= 0):
            setattr(instance, self.name, value)


class AutoSalon:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)


class Car:
    # YOUR CODE: Descriptors for name and price
    name = StringValue(2, 50)
    price = PriceValue(2000000)

    def __init__(self, name, price):
        self.name = name
        self.price = price


class TestClass:
    price = PriceValue(10000)

    def __init__(self, price):
        self.price = price
