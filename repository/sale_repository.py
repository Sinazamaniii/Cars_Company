import sqlite3
from model import Sale


class SaleRepository:
    def connect(self):
        self.connection = sqlite3.connect("../db/cars_co_db.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, sale):
        self.connect()
        self.cursor.execute(
            "insert into sales (sale_id, car_id, customer_id, employee_id, date, final_cost) values (?,?,?,?,?,?)",
            [sale.sale_id, sale.car_id, sale.customer_id, sale.employee_id, sale.date,
             sale.final_cost])
        sale.id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()
        return sale

    def update(self, sale):
        self.connect()
        self.cursor.execute(
            "update sales set sale_id = ?, car_id = ?, customer_id = ?, employee_id = ?, date = ?, final_cost = ? where id = ?",
            [sale.sale_id, sale.car_id, sale.customer_id, sale.employee_id, sale.date,
             sale.final_cost, sale.id])
        self.connection.commit()
        self.disconnect()
        return sale

    def delete(self, id):
        self.connect()
        self.cursor.execute(
            "delete from sales where id = ?",
            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from sales")
        sale_list = [Sale(*sale) for sale in self.cursor.fetchall()]
        self.disconnect()
        return sale_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute(
            "select * from employees where id = ?",
            [id])
        sale = self.cursor.fetchone()
        self.disconnect()
        if sale:
            return Sale(*sale)
        return None
