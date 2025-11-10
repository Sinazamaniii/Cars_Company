import sqlite3
from repository import DB_PATH
from model import Customer


class CustomerRepository:
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

    def save(self, customer):
        self.connect()
        self.cursor.execute(
            "insert into customers (customer_id, first_name, last_name, mobile_number, address) values (?,?,?,?,?)",
            [customer.customer_id, customer.first_name, customer.last_name, customer.mobile_number, customer.address])
        customer.id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()
        return customer

    def update(self, customer):
        self.connect()
        self.cursor.execute(
            "update customers set customer_id = ?, first_name = ?, last_name = ?, mobile_number = ?, address = ? where id = ?",
            [customer.customer_id, customer.first_name, customer.last_name, customer.mobile_number, customer.address,
             customer.id])
        self.connection.commit()
        self.disconnect()
        return customer

    def delete(self, id):
        self.connect()
        self.cursor.execute(
            "delete from customers where id = ?",
            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from customers")
        customer_list = [Customer(*customer) for customer in self.cursor.fetchall()]
        self.disconnect()
        return customer_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute(
            "select * from customers where id = ?",
            [id])
        customer = self.cursor.fetchone()
        self.disconnect()
        if customer:
            return Customer(*customer)
        return None
