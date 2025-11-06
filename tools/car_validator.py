import re
import datetime


def brand_validator(brand):
    if not (type(brand) == str and re.match(r"^[0-9a-zA-Z\s]{2,20}$", brand)):
        raise ValueError("Invalid brand !!!")
    else:
        return brand


def model_validator(model):
    if not (type(model) == str and re.match(r"^[0-9a-zA-Z\s]{2,20}$", model)):
        raise ValueError("Invalid model !!!")
    else:
        return model


def year_validator(year):
    current_year = datetime.datetime.now().year
    if not (str(year).isdigit() and 1886 <= int(year) <= current_year + 1):
        raise ValueError("Invalid year !!!")
    else:
        return int(year)


def price_validator(price):
    if not (type(price) == int or type(price) == float) or price <= 0:
        raise ValueError("Invalid price !!!")
    else:
        return price
