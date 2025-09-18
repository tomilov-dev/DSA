from uuid import uuid4

from src.mediator import Mediator
from src.service.order import OrderService
from src.service.billing import BillingService
from src.service.billing import BasicDiscountStrategy
from src.service.notification import NotificationService
from src.events import OrderEvent
from src.events import EventType
from src.models import Product
from src.models import OrderItem
from src.models import Order


def mock_ui_call(mediator: Mediator):
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
    mediator.publish(event)


if __name__ == "__main__":
    mediator = Mediator()
    order_service = OrderService(mediator)
    discount_strategy = BasicDiscountStrategy()
    billing_service = BillingService(mediator, discount_strategy)
    notification_service = NotificationService(mediator)

    mock_ui_call(mediator)
