from model import Customer
from service import CustomerService
from tools.logging import Logger


class CustomerController:
    @classmethod
    def save(cls, customer_id, first_name, last_name, mobile_number, address):
        try:
            customer = Customer(None, customer_id, first_name, last_name, mobile_number, address)
            customer.validate()
            customer = CustomerService.save(customer)
            Logger.info(f"Customer {customer} saved")
            return True, f"Customer Saved Successfully"
        except Exception as e:
            Logger.error(f"Customer Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, id, customer_id, first_name, last_name, mobile_number, address):
        try:
            customer = Customer(id, customer_id, first_name, last_name, mobile_number, address)
            customer.validate()
            customer = CustomerService.update(customer)
            Logger.info(f"Customer {customer} updated")
            return True, "Customer Updated Successfully"
        except Exception as e:
            Logger.error(f"Customer Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, id):
        try:
            customer = CustomerService.delete(id)
            Logger.info(f"Customer {customer} deleted")
            return True, f"Customer Deleted Successfully"
        except Exception as e:
            Logger.error(f"Customer Delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            customer_list = CustomerService.find_all()
            Logger.info("Customer FindAll")
            return True, customer_list
        except Exception as e:
            Logger.error(f"Customer FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, id):
        try:
            customer = CustomerService.find_by_id(id)
            Logger.info(f"Customer FindById {id}")
            return True, customer
        except Exception as e:
            Logger.error(f"{e} With Id {id}")
            return False, e
