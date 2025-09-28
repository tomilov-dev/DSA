from typing import Optional
from abc import ABC
from abc import abstractmethod
from .aggregate import Order


class IOrderRepository(ABC):
    @abstractmethod
    def save(self, order: Order) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, order_id: int) -> Optional[Order]:
        raise NotImplementedError
