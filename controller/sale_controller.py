from model import Sale
from service import SaleService
from tools import Logger

class SaleController:
    @classmethod
    def save(cls, car_id, customer_id, employee_id, date_time, final_cost):
        try:
            sale = Sale(None, car_id, customer_id, employee_id, date_time, final_cost)
            sale.validate()
            sale = SaleService.save(sale)
            Logger.info(f"Sale {sale} saved")
            return True, f"Sale Saved Successfully"
        except Exception as e:
            Logger.error(f"Sale Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, sale_id, car_id, customer_id, employee_id, date_time, final_cost):
        try:
            sale = Sale(sale_id, car_id, customer_id, employee_id, date_time, final_cost)
            sale.validate()
            sale = SaleService.update(sale)
            Logger.info(f"Sale {sale} updated")
            return True, "Sale Updated Successfully"
        except Exception as e:
            Logger.error(f"Sale Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, sale_id):
            try:
                sale = SaleService.delete(sale_id)
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
    def find_by_id(cls, sale_id):
        try:
            sale = SaleService.find_by_id(sale_id)
            Logger.info(f"Sale FindById {sale_id}")
            return True, sale
        except Exception as e:
            Logger.error(f"{e} With Id {sale_id}")
            return False, e