import re


def first_name_validator(first_name):
    if not (type(first_name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", first_name)):
        raise ValueError("Invalid first_name !!!")
    else:
        return first_name


def last_name_validator(last_name):
    if not (type(last_name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", last_name)):
        raise ValueError("Invalid last_name !!!")
    else:
        return last_name


def mobile_number_validator(mobile_number):
    if not (type(mobile_number) == str and re.match(r"^(09|\+989)\d{9}$", mobile_number)):
        raise ValueError("Invalid mobile_number !!!")
    else:
        return mobile_number


def address_validator(address):
    if not (type(address) == str and re.match(r"^[0-9a-zA-Z\s]{3,100}$", address)):
        raise ValueError("Invalid address !!!")
    else:
        return address
