from model import Car
from service import CarService
from tools import Logger

class CarController:
    @classmethod
    def save(cls, brand, model, year, price):
        try:
            car = Car(None, brand, model, year, price)
            car.validate()
            car = CarService.save(car)
            Logger.info(f"Car {car} saved")
            return True, f"Car Saved Successfully"
        except Exception as e:
            Logger.error(f"Car Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, car_id, brand, model, year, price):
        try:
            car = Car(car_id, brand, model, year, price)
            car.validate()
            car = CarService.update(car)
            Logger.info(f"Car {car} updated")
            return True, "Car Updated Successfully"
        except Exception as e:
            Logger.error(f"Car Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, car_id):
            try:
                car = CarService.delete(car_id)
                Logger.info(f"Car {car} deleted")
                return True, f"Car Deleted Successfully"
            except Exception as e:
                Logger.error(f"Car Delete Error: {e}")
                return False, e

    @classmethod
    def find_all(cls):
            try:
                car_list = CarService.find_all()
                Logger.info("Car FindAll")
                return True, car_list
            except Exception as e:
                Logger.error(f"Car FindAll Error: {e}")
                return False, e

    @classmethod
    def find_by_id(cls, car_id):
        try:
            car = CarService.find_by_id(car_id)
            Logger.info(f"Car FindById {car_id}")
            return True, car
        except Exception as e:
            Logger.error(f"{e} With Id {car_id}")
            return False, e


