from repository import CustomerRepository


class CustomerService:
    customer_repository = CustomerRepository()

    @classmethod
    def save(cls, customer):
        return cls.customer_repository.save(customer)

    @classmethod
    def update(cls, customer):
        customer_result = cls.customer_repository.find_by_id(customer.id)
        if customer_result:
            return cls.customer_repository.update(customer)
        else:
            raise Exception("Customer Not Found !!!")

    @classmethod
    def delete(cls, id):
        customer = cls.customer_repository.find_by_id(id)
        if customer:
            cls.customer_repository.delete(id)
            return customer
        else:
            raise Exception("Customer Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.customer_repository.find_all()

    @classmethod
    def find_by_id(cls, id):
        customer = cls.customer_repository.find_by_id(id)
        if customer:
            return customer
        else:
            raise Exception("Customer Not Found !!!")
