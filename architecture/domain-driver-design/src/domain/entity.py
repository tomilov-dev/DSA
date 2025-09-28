from typing import List


class OrderItem:
    def __init__(self, product_id: int, quantity: int):
        self.product_id = product_id
        self.quantity = quantity


class Customer:
    def __init__(self, customer_id: int, name: str):
        self.customer_id = customer_id
        self.name = name
