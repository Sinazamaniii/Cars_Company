import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "db", "cars_co_db.db")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

from repository.car_repository import CarRepository
from repository.customer_repository import CustomerRepository
from repository.employee_repository import EmployeeRepository
from repository.maintenance_repository import MaintenanceRepository
from repository.sale_repository import SaleRepository
