from tools.employee_validator import *


class Employee:
    def __init__(self, id, employee_id, first_name, last_name, occupation, username, password):
        self.id = id
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.username = username
        self.password = password

    def validate(self):
        first_name_validator(self.first_name)
        last_name_validator(self.last_name)
        occupation_validator(self.occupation)
        username_validator(self.username)
        password_validator(self.password)

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(
            (self.id, self.employee_id, self.first_name, self.last_name, self.occupation, self.username, self.password))
