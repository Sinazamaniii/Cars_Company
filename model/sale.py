from tools.sale_validator import *


class Sale:
    def __init__(self, id, sale_id, car_id, customer_id, employee_id, date_time, final_cost):
        self.id = id
        self.sale_id = sale_id
        self.car_id = car_id
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.date_time = date_time
        self.final_cost = final_cost

    def validate(self):
        car_id_validator(self.car_id)
        customer_id_validator(self.customer_id)
        employee_id_validator(self.employee_id)
        date_time_validator(self.date_time)
        final_cost_validator(self.final_cost)

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple(
            (self.id, self.sale_id, self.car_id, self.customer_id, self.employee_id, self.date_time, self.final_cost))
