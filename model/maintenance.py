from tools.maintenance_validator import *


class Maintenance:
    def __init__(self, id, maintenance_id, car_id, employee_id, service_type, cost):
        self.id = id
        self.maintenance_id = maintenance_id
        self.car_id = car_id
        self.employee_id = employee_id
        self.service_type = service_type
        self.cost = cost

    def validate(self):
        car_id_validator(self.car_id)
        employee_id_validator(self.employee_id)
        service_type_validator(self.service_type)
        cost_validator(self.cost)

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.id, self.maintenance_id, self.car_id, self.employee_id, self.service_type, self.cost))
