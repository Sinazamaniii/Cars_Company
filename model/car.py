from tools.car_validator import *


class Car:
    def __init__(self, car_id, brand, model, year, price):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price

    def validate(self):
        brand_validator(self.brand)
        model_validator(self.model)
        year_validator(self.year)
        price_validator(self.price)


    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.car_id, self.brand, self.model, self.year, self.price))