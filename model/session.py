class Session:
    employee = None
    customer = None
    maintenance = []
    sale = None

    @classmethod
    def add_maintenance(cls, maintenance):
        cls.maintenance.append(maintenance)
