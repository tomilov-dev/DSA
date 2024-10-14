from abc import ABC
from abc import abstractmethod


class ProductServiceInterface(ABC):
    @abstractmethod
    def get_product_details(self, product_id: str) -> dict:
        pass


class OldProductService:
    def get_product_details(self, product_id: str) -> dict:
        return {"name": "Product1", "price": 100}


class NewProductService:
    def retrieve_product(self, product_id: str) -> dict:
        return {"product_name": "Product1", "product_price": 100}


class ProductServiceAdapter(ProductServiceInterface):
    def __init__(self, product_service: NewProductService) -> None:
        self.product_service = product_service

    def get_product_details(self, product_id: str) -> dict:
        data = self.product_service.retrieve_product(product_id)
        return {"name": data["product_name"], "price": data["product_price"]}


def client_code():
    old_service = OldProductService()
    new_service = ProductServiceAdapter(NewProductService())

    product_id = "12345"
    print(
        f"Product details (old service): {old_service.get_product_details(product_id)}"
    )
    print(
        f"Product details (new service): {new_service.get_product_details(product_id)}"
    )
