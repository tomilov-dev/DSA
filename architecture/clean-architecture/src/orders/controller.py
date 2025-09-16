import sys
from pathlib import Path
from abc import ABC
from abc import abstractmethod


PROJ_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(PROJ_DIR))
from src.orders.order import IOrder
from src.orders.service import OrderDTO
from src.orders.service import IGetOrderUseCase
from src.orders.service import IConfirmOrderUseCase


class IOrderController(ABC):
    def __init__(
        self,
        get_order_use_case: IGetOrderUseCase,
        confirm_order_use_case: IConfirmOrderUseCase,
    ) -> None:
        self._get_order_use_case = get_order_use_case
        self._confirm_order_use_case = confirm_order_use_case

    @abstractmethod
    def get_order_by_id(self, order_id: str) -> OrderDTO:
        pass

    @abstractmethod
    def confirm_order_by_id(self, order_id: str) -> None:
        pass


class OrderController(IOrderController):
    def get_order_by_id(self, order_id: str) -> OrderDTO:
        return self._get_order_use_case.execute(order_id)

    def confirm_order_by_id(self, order_id: str) -> None:
        return self._confirm_order_use_case.execute(order_id)
