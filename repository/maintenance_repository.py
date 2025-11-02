import sqlite3
from model import Maintenance


class MaintenanceRepository:
    def connect(self):
        self.connection = sqlite3.connect("../db/cars_co_db.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, maintenance):
        self.connect()
        self.cursor.execute(
            "insert into maintenances (maintenance_id, car_id, employee_id, service_type, cost) values (?,?,?,?,?)",
            [maintenance.maintenance_id, maintenance.car_id, maintenance.employee_id, maintenance.service_type,
             maintenance.cost])
        maintenance.id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()
        return maintenance

    def update(self, maintenance):
        self.connect()
        self.cursor.execute(
            "update maintenances set maintenance_id = ?, car_id = ?, employee_id = ?, service_type = ?, cost = ? where id = ?",
            [maintenance.maintenance_id, maintenance.car_id, maintenance.employee_id, maintenance.service_type,
             maintenance.cost, maintenance.id])
        self.connection.commit()
        self.disconnect()
        return maintenance

    def delete(self, id):
        self.connect()
        self.cursor.execute(
            "delete from maintenances where id = ?",
            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from maintenances")
        maintenance_list = [Maintenance(*maintenance) for maintenance in self.cursor.fetchall()]
        self.disconnect()
        return maintenance_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute(
            "select * from maintenances where id = ?",
            [id])
        maintenance = self.cursor.fetchone()
        self.disconnect()
        if maintenance:
            return Maintenance(*maintenance)
        return None
