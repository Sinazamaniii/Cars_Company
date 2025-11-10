from repository import EmployeeRepository


class EmployeeService:
    employee_repository = EmployeeRepository()

    @classmethod
    def save(cls, employee):
        return cls.employee_repository.save(employee)

    @classmethod
    def update(cls, employee):
        employee_result = cls.employee_repository.find_by_id(employee.id)
        if employee_result:
            return cls.employee_repository.update(employee)
        else:
            raise Exception("Employee Not Found !!!")

    @classmethod
    def delete(cls, id):
        employee = cls.employee_repository.find_by_id(id)
        if employee:
            cls.employee_repository.delete(id)
            return employee
        else:
            raise Exception("Employee Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.employee_repository.find_all()

    @classmethod
    def find_by_id(cls, id):
        employee = cls.employee_repository.find_by_id(id)
        if employee:
            return employee
        else:
            raise Exception("Employee Not Found !!!")

    @classmethod
    def find_by_username_and_password(cls, username, password):
        return cls.employee_repository.find_by_username_and_password(username, password)
