from uuid import uuid4
import time

from src.broker import IEventBroker
from src.broker import InMemoryEventBroker
from src.service.order import OrderService
from src.service.billing import BillingSerivce
from src.service.billing import BasicDiscountStrategy
from src.service.notification import NotificationService
from src.events import EventType
from src.events import OrderEvent

from src.models import Product
from src.models import OrderItem
from src.models import Order


def mock_ui_call(broker: IEventBroker):
    order = Order(
        id=uuid4().hex,
        items=[
            OrderItem(product=Product("Product1", price=50), quantity=5),
            OrderItem(product=Product("Product2", price=65), quantity=4),
        ],
    )
    event = OrderEvent(
        id=uuid4().hex,
        type=EventType.ORDER,
        order=order,
    )
    broker.push(event)


if __name__ == "__main__":
    broker = InMemoryEventBroker()
    order_service = OrderService(broker)
    discount_strategy = BasicDiscountStrategy()
    billing_service = BillingSerivce(broker, discount_strategy)
    notification_service = NotificationService(broker)

    mock_ui_call(broker)

    while True:
        order_service.listen()
        billing_service.listen()
        notification_service.listen()
