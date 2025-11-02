


class Maintenance:
    def __init__(self, maintenance_id, car_id, employee_id, service_type, cost):
        self.maintenance_id = maintenance_id
        self.car_id = car_id
        self.employee_id = employee_id
        self.service_type = service_type
        self.cost = cost







    def __repr__(self):
        return f"{self.__dict__}"
