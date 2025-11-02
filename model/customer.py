


class Customer:
    def __init__(self, customer_id, first_name, last_name, mobile_number, address):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.mobile_number = mobile_number
        self.address = address










    def __repr__(self):
            return f"{self.__dict__}"