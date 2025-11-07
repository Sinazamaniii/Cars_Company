from model import Sale
from service import SaleService
from tools import Logger


class SaleController:
    @classmethod
    def save(cls, sale_id, car_id, customer_id, employee_id, date_time, final_cost):
        try:
            sale = Sale(None, sale_id, car_id, customer_id, employee_id, date_time, final_cost)
            sale.validate()
            sale = SaleService.save(sale)
            Logger.info(f"Sale {sale} saved")
            return True, f"Sale Saved Successfully"
        except Exception as e:
            Logger.error(f"Sale Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, id, sale_id, car_id, customer_id, employee_id, date_time, final_cost):
        try:
            sale = Sale(id, sale_id, car_id, customer_id, employee_id, date_time, final_cost)
            sale.validate()
            sale = SaleService.update(sale)
            Logger.info(f"Sale {sale} updated")
            return True, "Sale Updated Successfully"
        except Exception as e:
            Logger.error(f"Sale Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, id):
        try:
            sale = SaleService.delete(id)
            Logger.info(f"Sale {sale} deleted")
            return True, f"Sale Deleted Successfully"
        except Exception as e:
            Logger.error(f"Sale Delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            sale_list = SaleService.find_all()
            Logger.info("Sale FindAll")
            return True, sale_list
        except Exception as e:
            Logger.error(f"Sale FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, id):
        try:
            sale = SaleService.find_by_id(id)
            Logger.info(f"Sale FindById {id}")
            return True, sale
        except Exception as e:
            Logger.error(f"{e} With Id {id}")
            return False, e
