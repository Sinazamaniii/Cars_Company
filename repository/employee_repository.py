import sqlite3
from repository import DB_PATH
from model import Employee


class EmployeeRepository:
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

    def save(self, employee):
        self.connect()
        self.cursor.execute(
            "insert into employees (employee_id, first_name, last_name, occupation, username, password) values (?,?,?,?,?,?)",
            [employee.employee_id, employee.first_name, employee.last_name, employee.occupation, employee.username,
             employee.password])
        employee.id = self.cursor.lastrowid
        self.connection.commit()
        self.disconnect()
        return employee

    def update(self, employee):
        self.connect()
        self.cursor.execute(
            "update employees set employee_id = ?, first_name = ?, last_name = ?, occupation = ?, username = ?, password = ? where id = ?",
            [employee.employee_id, employee.first_name, employee.last_name, employee.occupation, employee.username,
             employee.password, employee.id])
        self.connection.commit()
        self.disconnect()
        return employee

    def delete(self, id):
        self.connect()
        self.cursor.execute(
            "delete from employees where id = ?",
            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from employees")
        employee_list = [Employee(*employee) for employee in self.cursor.fetchall()]
        self.disconnect()
        return employee_list

    def find_by_id(self, id):
        self.connect()
        self.cursor.execute(
            "select * from employees where id = ?",
            [id])
        employee = self.cursor.fetchone()
        self.disconnect()
        if employee:
            return Employee(*employee)
        return None

    def find_by_username_and_password(self, username, password):
        self.connect()
        self.cursor.execute("select * from employees where username=?", [username])
        row = self.cursor.fetchone()
        self.disconnect()
        if row:
            return True, Employee(*row)
        return False, None
