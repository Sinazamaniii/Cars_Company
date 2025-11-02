


class Employee:
    def __init__(self, employee_id, first_name, last_name, occupation, username, password):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.username = username
        self.password = password








    def __repr__(self):
        return f"{self.__dict__}"