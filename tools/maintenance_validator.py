import re


def car_id_validator(car_id):
    if not (type(car_id) == int and car_id > 0):
        raise ValueError("Invalid car_id !!!")
    else:
        return car_id


def employee_id_validator(employee_id):
    if not (type(employee_id) == int and employee_id > 0):
        raise ValueError("Invalid employee_id !!!")
    else:
        return employee_id


def service_type_validator(service_type):
    if not (type(service_type) == str and re.match(r"^[a-zA-Z\s]{3,30}$", service_type)):
        raise ValueError("Invalid service_type !!!")
    else:
        return service_type


def cost_validator(cost):
    if not (type(cost) in [int, float] and cost > 0):
        raise ValueError("Invalid cost !!!")
    else:
        return float(cost)
