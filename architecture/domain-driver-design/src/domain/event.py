from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class OrderPlacedEvent:
    order_id: int
    occurred_on: datetime
