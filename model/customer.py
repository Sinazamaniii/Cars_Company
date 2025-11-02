from tools.customer_validator import *


class Customer:
    def __init__(self, customer_id, first_name, last_name, mobile_number, address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number
        self.address = address

    def validate(self):
        first_name_validator(self.first_name)
        last_name_validator(self.last_name)
        mobile_number_validator(self.mobile_number)
        address_validator(self.address)



    def __repr__(self):
            return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.customer_id, self.first_name, self.last_name, self.mobile_number, self.address))