from repository import CarRepository


class CarService:
    car_repository = CarRepository()

    @classmethod
    def save(cls, car):
        return cls.car_repository.save(car)

    @classmethod
    def update(cls, car):
        car_result = cls.car_repository.find_by_id(car.id)
        if car_result:
            return cls.car_repository.update(car)
        else:
            raise Exception("Car Not Found !!!")

    @classmethod
    def delete(cls, id):
        car = cls.car_repository.find_by_id(id)
        if car:
            cls.car_repository.delete(id)
            return car
        else:
            raise Exception("Car Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.car_repository.find_all()

    @classmethod
    def find_by_id(cls, id):
        car = cls.car_repository.find_by_id(id)
        if car:
            return car
        else:
            raise Exception("Car Not Found !!!")
