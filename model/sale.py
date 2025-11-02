


class Sale:
    def __init__(self, sale_id, car_id, customer_id, employee_id, date, final_cost):
        self.sale_id = sale_id
        self.car_id = car_id
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.date = date
        self.final_cost = final_cost






    def __repr__(self):
        return f"{self.__dict__}"