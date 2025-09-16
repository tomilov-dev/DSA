import sys
from pathlib import Path
from abc import ABC
from abc import abstractmethod
from pydantic import BaseModel


PROJ_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(PROJ_DIR))
from src.shared.logger import ILogger
from src.shared.alert import IAlertManager
from src.orders.order import Product
from src.orders.order import IOrderItem
from src.orders.order import OrderItem
from src.orders.order import IOrder
from src.orders.order import Order


class OrderNotFound(Exception):
    pass


class UseCaseUnexpectedError(Exception):
    pass


class ProductDTO(BaseModel):
    id: str
    name: str
    price: str


class OrderItemDTO(BaseModel):
    product: ProductDTO
    quantity: int


class OrderDTO(BaseModel):
    id: str
    items: list[OrderItemDTO]


class IOrderMapper(ABC):
    @abstractmethod
    def from_dto(self, order_dto: OrderDTO) -> IOrder:
        pass

    @abstractmethod
    def to_dto(self, order: IOrder) -> OrderDTO:
        pass


class OrderMapper(IOrderMapper):
    def from_dto(self, order_dto: OrderDTO) -> IOrder:
        items: list[IOrderItem] = [
            OrderItem(
                product=Product(
                    id=i.product.id, name=i.product.name, price=float(i.product.price)
                ),
                quantity=i.quantity,
            )
            for i in order_dto.items
        ]
        return Order(order_id=order_dto.id, items=items)

    def to_dto(self, order: IOrder) -> OrderDTO:
        items = [
            OrderItemDTO(
                product=ProductDTO(
                    id=item.product.id,
                    name=item.product.name,
                    price=str(item.product.price),
                ),
                quantity=item.quantity,
            )
            for item in order.items
        ]
        return OrderDTO(id=order.order_id, items=items)


class IOrderRepository(ABC):
    def __init__(
        self,
        logger: ILogger,
        alert: IAlertManager,
    ) -> None:
        self._logger = logger
        self._alert = alert

    @abstractmethod
    def get_by_id(self, order_id: str) -> OrderDTO | None:
        pass

    @abstractmethod
    def save(self, order: OrderDTO) -> None:
        pass


class BasicUseCase:
    def __init__(
        self,
        logger: ILogger,
        alert: IAlertManager,
    ) -> None:
        self._logger = logger
        self._alert = alert


class IGetOrderUseCase(ABC, BasicUseCase):
    @abstractmethod
    def execute(self, order_id: str) -> OrderDTO:
        pass


class IConfirmOrderUseCase(ABC, BasicUseCase):
    @abstractmethod
    def execute(self, order_id: str) -> None:
        pass


class GetOrderUseCase(IGetOrderUseCase):
    def __init__(
        self,
        logger: ILogger,
        alert: IAlertManager,
        order_repository: IOrderRepository,
        order_mapper: IOrderMapper,
    ) -> None:
        super().__init__(logger, alert)
        self._repository = order_repository
        self._mapper = order_mapper

    def execute(self, order_id: str) -> OrderDTO:
        try:
            order_dto = self._repository.get_by_id(order_id)
            if order_dto is None:
                raise OrderNotFound(f"Order not found: {order_id}")
            return order_dto
        except Exception as ex:
            self._logger.critical(f"Error in GetOrderUseCase: {ex}")
            self._alert.alert(f"Error in GetOrderUseCase: {ex}")
            raise UseCaseUnexpectedError from ex


class ConfirmOrderUseCase(IConfirmOrderUseCase):
    def __init__(
        self,
        logger: ILogger,
        alert: IAlertManager,
        order_repository: IOrderRepository,
        order_mapper: IOrderMapper,
    ) -> None:
        super().__init__(logger, alert)
        self._repository = order_repository
        self._mapper = order_mapper

    def execute(self, order_id: str) -> None:
        try:
            order_dto = self._repository.get_by_id(order_id)
            if order_dto is None:
                raise OrderNotFound(f"Order not found: {order_id}")

            order = self._mapper.from_dto(order_dto)
            order.confirm()
            order_dto = self._mapper.to_dto(order)

            self._repository.save(order_dto)
        except Exception as ex:
            self._logger.error(f"Error in ConfirmOrderUseCase: {ex}")
            self._alert.alert(f"Error in ConfirmOrderUseCase: {ex}")
            raise UseCaseUnexpectedError from ex
