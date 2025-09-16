import sys
from pathlib import Path


PROJ_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(PROJ_DIR))
from src.shared.logger import ILogger
from src.shared.alert import IAlertManager
from src.orders.service import OrderDTO
from src.orders.service import IOrderRepository


class InMemoryOrderRepository(IOrderRepository):
    def __init__(
        self,
        logger: ILogger,
        alert: IAlertManager,
    ) -> None:
        super().__init__(logger, alert)
        self.orders = {}

    def get_by_id(self, order_id: str) -> OrderDTO | None:
        return self.orders.get(order_id, None)

    def save(self, order: OrderDTO) -> None:
        self.orders[order.id] = order
