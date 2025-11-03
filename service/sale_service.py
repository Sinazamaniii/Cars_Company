from repository import SaleRepository


class SaleService:
    sale_repository = SaleRepository()

    @classmethod
    def save(cls, sale):
        return cls.sale_repository.save(sale)

    @classmethod
    def update(cls, sale):
        sale_result = cls.sale_repository.find_by_id(sale.sale_id)
        if sale_result:
            return cls.sale_repository.update(sale)
        else:
            raise Exception("Sale Not Found !!!")

    @classmethod
    def delete(cls, sale_id):
        sale = cls.sale_repository.find_by_id(sale_id)
        if sale:
            cls.sale_repository.delete(sale_id)
            return sale
        else:
            raise Exception("Sale Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.sale_repository.find_all()

    @classmethod
    def find_by_id(cls, sale_id):
        sale = cls.sale_repository.find_by_id(sale_id)
        if sale:
            return sale
        else:
            raise Exception("Sale Not Found !!!")