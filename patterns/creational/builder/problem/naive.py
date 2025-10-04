"""
Решение задачи конструктора тарифов мобильной связи
"""

from enum import Enum
from abc import ABC
from abc import abstractmethod


class InternetSpeed(str, Enum):
    SLOW = "Slow"
    MEDIUM = "Medium"
    FAST = "Fast"


DEFAULT_SPEED_COST = {
    InternetSpeed.SLOW: 0.75,
    InternetSpeed.MEDIUM: 1,
    InternetSpeed.FAST: 1.25,
}


class Minutes:
    def __init__(
        self,
        amount: int,
    ) -> None:
        self.amount = amount


class Internet:
    def __init__(
        self,
        amount: int,
        speed: InternetSpeed,
    ) -> None:
        self.amount = amount
        self.speed = speed


class Messages:
    def __init__(
        self,
        amount: int,
    ) -> None:
        self.amount = amount


class AddOn:
    def __init__(
        self,
        name: str,
        price: float,
    ) -> None:
        self.name = name
        self.price = price


class TarrifConfig:
    def __init__(
        self,
        minute_cost: float,
        internet_cost: float,
        message_cost: float,
        speed_cost: dict[InternetSpeed, float],
        roaming_kf: float = 1,
    ):
        self.minute_cost = minute_cost
        self.internet_cost = internet_cost
        self.message_cost = message_cost
        self.speed_cost = speed_cost
        self.roaming_kf = roaming_kf


class ITarrif(ABC):
    @abstractmethod
    def calculate_total(
        self,
        minutes: Minutes,
        internet: Internet,
        messages: Messages,
        add_ons: list[AddOn],
        config: TarrifConfig,
    ) -> float:
        pass

    @abstractmethod
    def total(self) -> float:
        pass


class TarrifBase(ITarrif):
    def calculate_total(
        self,
        minutes: Minutes,
        internet: Internet,
        messages: Messages,
        add_ons: list[AddOn],
        config: TarrifConfig,
    ) -> float:
        spc = config.speed_cost
        rkf = config.roaming_kf
        itc = config.internet_cost * internet.amount * spc[internet.speed] * rkf
        return sum(
            [
                config.minute_cost * minutes.amount * rkf,
                itc,
                config.message_cost * messages.amount * rkf,
                sum(ad.price for ad in add_ons),
            ]
        )


## Изначально есть два тарифа: базовый и специальный
class BaseTarrif(TarrifBase):
    def __init__(
        self,
        minutes: Minutes,
        internet: Internet,
        messages: Messages,
        add_ons: list[AddOn],
    ) -> None:
        self.minutes = minutes
        self.internet = internet
        self.messages = messages
        self.add_ons = add_ons

    def total(self) -> float:
        return self.calculate_total(
            minutes=self.minutes,
            internet=self.internet,
            messages=self.messages,
            add_ons=self.add_ons,
            config=TarrifConfig(2, 6, 1, DEFAULT_SPEED_COST),
        )


class SpecialTarrifValidationError(Exception):
    pass


class SpecialTarrif(TarrifBase):
    def __init__(
        self,
        minutes: Minutes,
        internet: Internet,
        messages: Messages,
        add_ons: list[AddOn],
    ) -> None:
        if minutes.amount < 350:
            raise SpecialTarrifValidationError(
                "Special Tarrif minutes amount can't be less than 350"
            )
        if internet.amount < 30:
            raise SpecialTarrifValidationError(
                "Special Tarrif internet amount can't be less than 30"
            )
        if internet.speed == InternetSpeed.SLOW:
            raise SpecialTarrifValidationError(
                "Special Tarrif internet speed can't be slow"
            )
        if messages.amount < 100:
            raise SpecialTarrifValidationError(
                "Special Tarrif messages amount can't be less than 100"
            )

        self.minutes = minutes
        self.internet = internet
        self.messages = messages
        self.add_ons = add_ons

    def total(self) -> float:
        return self.calculate_total(
            minutes=self.minutes,
            internet=self.internet,
            messages=self.messages,
            add_ons=self.add_ons,
            config=TarrifConfig(
                1.5,
                5,
                0.7,
                {
                    InternetSpeed.MEDIUM: 0.9,
                    InternetSpeed.FAST: 1.1,
                },
            ),
        )


class Roaming:
    def __init__(
        self,
        country: str,
        kf: float,
    ) -> None:
        self.country = country
        self.kf = kf


## Добавляем новый тариф без дополнений и с роумингом
class RoamingTarrif(TarrifBase):
    def __init__(
        self,
        minutes: Minutes,
        internet: Internet,
        messages: Messages,
        roaming: Roaming,
    ) -> None:
        self.minutes = minutes
        self.internet = internet
        self.messages = messages
        self.roaming = roaming

    def total(self) -> float:
        return self.calculate_total(
            minutes=self.minutes,
            internet=self.internet,
            messages=self.messages,
            add_ons=[],
            config=TarrifConfig(
                2,
                6,
                1,
                DEFAULT_SPEED_COST,
                roaming_kf=self.roaming.kf,
            ),
        )


def client_code():
    base = BaseTarrif(
        minutes=Minutes(100),
        internet=Internet(15, InternetSpeed.MEDIUM),
        messages=Messages(50),
        add_ons=[AddOn("Музыкальный звонок", 50)],
    )
    print(base.total())

    special = SpecialTarrif(
        minutes=Minutes(350),
        internet=Internet(30, InternetSpeed.MEDIUM),
        messages=Messages(100),
        add_ons=[AddOn("Музыкальный звонок", 50)],
    )
    print(special.total())

    roaming = RoamingTarrif(
        minutes=Minutes(100),
        internet=Internet(10, InternetSpeed.MEDIUM),
        messages=Messages(50),
        roaming=Roaming("US", 2),
    )
    print(roaming.total())


if __name__ == "__main__":
    client_code()
