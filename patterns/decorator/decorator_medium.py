from abc import ABC, abstractmethod


class OrderProcessor(ABC):
    @abstractmethod
    def process(self, order: dict) -> dict:
        pass


class BaseOrderProcessor(OrderProcessor):
    def process(self, order: dict) -> dict:
        return order


class OrderProcessorDecorator(OrderProcessor):
    def __init__(self, processor: OrderProcessor) -> None:
        self.processor = processor

    def process(self, order: dict) -> dict:
        return self.processor.process(order)


class DiscountDecorator(OrderProcessorDecorator):
    def __init__(self, processor: OrderProcessor, discount: float) -> None:
        super().__init__(processor)
        self.discount = discount

    def process(self, order: dict) -> dict:
        order["discount"] = self.discount
        if "price" in order:
            order["discount_price"] = order["price"] * (1 - self.discount)
        return self.processor.process(order)


class TaxDecorator(OrderProcessorDecorator):
    def __init__(self, processor: OrderProcessor, tax: float) -> None:
        super().__init__(processor)
        self.tax = tax

    def process(self, order: dict) -> dict:
        if "price" in order:
            order["tax_amount"] = order["price"] * self.tax
            order["price_with_tax"] = order["price"] + order["tax_amount"]
        return self.processor.process(order)


class ShippingDecorator(OrderProcessorDecorator):
    def __init__(self, processor: OrderProcessor, shipping_cost: float) -> None:
        super().__init__(processor)
        self.shipping_cost = shipping_cost

    def process(self, order: dict) -> dict:
        order["shipping_cost"] = self.shipping_cost
        if "price" in order:
            order["total_price"] = order["price"] + self.shipping_cost
        return self.processor.process(order)


def client_code():
    base_processor = BaseOrderProcessor()

    processor_with_discount = DiscountDecorator(base_processor, discount=0.1)
    processor_with_tax = TaxDecorator(processor_with_discount, tax=0.2)
    processor_with_shipping = ShippingDecorator(processor_with_tax, shipping_cost=5.0)

    order = {"price": 100.0}
    processed_order = processor_with_shipping.process(order)
    print(processed_order)
