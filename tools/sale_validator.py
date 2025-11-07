import re


def car_id_validator(car_id):
    if not (type(car_id) == int and car_id > 0):
        raise ValueError("Invalid car_id !!!")
    else:
        return car_id


def customer_id_validator(customer_id):
    if not (type(customer_id) == int and customer_id > 0):
        raise ValueError("Invalid customer_id !!!")
    else:
        return customer_id


def employee_id_validator(employee_id):
    if not (type(employee_id) == int and employee_id > 0):
        raise ValueError("Invalid employee_id !!!")
    else:
        return employee_id


def date_time_validator(date_time):
    if not (type(date_time) == str and re.match(r"^\d{2}[/-]\d{2}[/-]\d{4}\s\d{2}:\d{2}(:\d{2})$", date_time)):
        raise ValueError("Invalid Date Time !!!")
    else:
        return date_time


def final_cost_validator(final_cost):
    if not (type(final_cost) == int and final_cost > 0):
        raise ValueError("Invalid Final Cost !!!")
    else:
        return final_cost
