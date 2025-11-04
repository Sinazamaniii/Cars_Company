from model import Maintenance
from service import MaintenanceService
from tools import Logger

class MaintenanceController:
    @classmethod
    def save(cls, car_id, employee_id, service_type, cost):
        try:
            maintenance = Maintenance(None, car_id, employee_id, service_type, cost)
            maintenance.validate()
            maintenance = MaintenanceService.save(maintenance)
            Logger.info(f"Maintenance {maintenance} saved")
            return True, f"Maintenance Saved Successfully"
        except Exception as e:
            Logger.error(f"Maintenance Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, maintenance_id, car_id, employee_id, service_type, cost):
        try:
            maintenance = Maintenance(maintenance_id, car_id, employee_id, service_type, cost)
            maintenance.validate()
            maintenance = MaintenanceService.update(maintenance)
            Logger.info(f"Maintenance {maintenance} updated")
            return True, "Maintenance Updated Successfully"
        except Exception as e:
            Logger.error(f"Maintenance Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, maintenance_id):
        try:
            maintenance = MaintenanceService.delete(maintenance_id)
            Logger.info(f"Maintenance {maintenance} deleted")
            return True, f"Maintenance Deleted Successfully"
        except Exception as e:
            Logger.error(f"Maintenance Delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            maintenance_list = MaintenanceService.find_all()
            Logger.info("Maintenance FindAll")
            return True, maintenance_list
        except Exception as e:
            Logger.error(f"Maintenance FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, maintenance_id):
        try:
            maintenance = MaintenanceService.find_by_id(maintenance_id)
            Logger.info(f"Maintenance FindById {maintenance_id}")
            return True, maintenance
        except Exception as e:
            Logger.error(f"{e} With Id {maintenance_id}")
            return False, e