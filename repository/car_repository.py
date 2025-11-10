import sqlite3
from repository import DB_PATH
from model import Car


class CarRepository:
    def __init__(self):
        self.db_path = DB_PATH
        self.connection = None
        self.cursor = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, car):
        self.connect()
        self.cursor.execute(
            "insert into cars (car_id, brand, model, year, price) values (?,?,?,?,?)",
            [car.car_id, car.brand, car.model, car.year, car.price])
        car.id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()
        return car

    def update(self, car):
        self.connect()
        self.cursor.execute(
            "update cars set car_id = ?, brand = ?, model = ?, year = ?, price = ? where id = ?",
            [car.car_id, car.brand, car.model, car.year, car.price, car.id])
        self.connection.commit()
        self.disconnect()
        return car

    def delete(self, id):
        self.connect()
        self.cursor.execute(
            "delete from cars where id = ?",
            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from cars")
        car_list = [Car(*car) for car in self.cursor.fetchall()]
        self.disconnect()
        return car_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute(
            "select * from cars where id = ?",
            [id])
        car = self.cursor.fetchone()
        self.disconnect()
        if car:
            return Car(*car)
        return None
