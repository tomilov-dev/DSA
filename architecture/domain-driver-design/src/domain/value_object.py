from dataclasses import dataclass


@dataclass(frozen=True)
class Address:
    street: str
    city: str

    def is_valid(self) -> bool:
        return bool(self.street and self.city)
