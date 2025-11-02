


class Car:
    def __init__(self, car_id, brand, model, year, price):
        self.car_id = car_id
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price










    def __repr__(self):
        return f"{self.__dict__}"