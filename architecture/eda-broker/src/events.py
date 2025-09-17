from enum import Enum
from abc import ABC
from abc import abstractmethod
from typing import Any

from src.models import Order


class EventType(str, Enum):
    ORDER = "ORDER"
    BILLING = "BILLING"
    NOTIFICATION = "NOTIFICATION"


class IEvent(ABC):
    def __init__(self, id: str, type: EventType) -> None:
        self._id = id
        self._type = type

    @property
    def id(self) -> str:
        return self._id

    @property
    def type(self) -> EventType:
        return self._type


class OrderEvent(IEvent):
    def __init__(self, id: str, type: EventType, order: Order) -> None:
        super().__init__(id, type)
        self._order = order

    @property
    def order(self) -> Order:
        return self._order


class BillingEvent(IEvent):
    def __init__(self, id: str, type: EventType, order: Order) -> None:
        super().__init__(id, type)
        self._order = order

    @property
    def order(self) -> Order:
        return self._order


class NotificationEvent(IEvent):
    def __init__(
        self,
        id: str,
        type: EventType,
        order: Order,
        discount: float,
        total: float,
    ) -> None:
        super().__init__(id, type)
        self._order = order
        self._discount = discount
        self._total = total

    @property
    def order(self) -> Order:
        return self._order

    @property
    def total(self) -> float:
        return self._total

    @property
    def discount(self) -> float:
        return self._discount
