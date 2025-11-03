from repository import MaintenanceRepository


class MaintenanceService:
    maintenance_repository = MaintenanceRepository()

    @classmethod
    def save(cls, maintenance):
        return cls.maintenance_repository.save(maintenance)

    @classmethod
    def update(cls, maintenance):
        maintenance_result = cls.maintenance_repository.find_by_id(maintenance.maintenance_id)
        if maintenance_result:
            return cls.maintenance_repository.update(maintenance)
        else:
            raise Exception("Maintenance Not Found !!!")

    @classmethod
    def delete(cls, maintenance_id):
        maintenance = cls.maintenance_repository.find_by_id(maintenance_id)
        if maintenance:
            cls.maintenance_repository.delete(maintenance_id)
            return maintenance
        else:
            raise Exception("Maintenance Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.maintenance_repository.find_all()

    @classmethod
    def find_by_id(cls, maintenance_id):
        maintenance = cls.maintenance_repository.find_by_id(maintenance_id)
        if maintenance:
            return maintenance
        else:
            raise Exception("Maintenance Not Found !!!")