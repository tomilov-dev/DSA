from src.domain.entity import OrderItem, Customer
from src.domain.value_object import Address
from src.domain.aggregate import Order
from src.infrastructure.in_memory_repository import InMemoryOrderRepository
from src.application.place_order import PlaceOrderUseCase


def main():
    customer = Customer(customer_id=1, name="Ivan Ivanov")
    address = Address(street="Lenina 1", city="Moscow")
    items = [
        OrderItem(product_id=101, quantity=2),
        OrderItem(product_id=102, quantity=1),
    ]

    order = Order(order_id=1, customer=customer, address=address, items=items)

    repository = InMemoryOrderRepository()
    place_order = PlaceOrderUseCase(repository)

    try:
        event = place_order.execute(order)
        print(f"Order placed: {event}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
