"""
Решение задачи конструктора тарифов мобильной связи с паттерном Builder
"""

from enum import Enum
from abc import ABC
from abc import abstractmethod


class InternetSpeed(str, Enum):
    SLOW = "Slow"
    MEDIUM = "Medium"
    FAST = "Fast"


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


class ITarrifBuilder(ABC):
    def __init__(self):
        self.reset()

    @abstractmethod
    def build_minutes(self):
        pass

    @abstractmethod
    def build_internet(self):
        pass

    @abstractmethod
    def build_messages(self):
        pass

    @abstractmethod
    def build_add_ons(self):
        pass

    @abstractmethod
    def reset(self):
        pass


class TarrifConfig:
    def __init__(
        self,
        minute_cost: float,
        internet_cost: float,
        message_cost: float,
        speed_cost: dict[InternetSpeed, float] | None = None,
        roaming_kf: float = 1,
    ):
        self.minute_cost = minute_cost
        self.internet_cost = internet_cost
        self.message_cost = message_cost
        self.speed_cost = speed_cost
        self.roaming_kf = roaming_kf
        if self.speed_cost is None:
            self.speed_cost = {
                InternetSpeed.SLOW: 0.75,
                InternetSpeed.MEDIUM: 1,
                InternetSpeed.FAST: 1.25,
            }


class TarrifBase(ABC):
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


class TarrifBuilderBase(ITarrifBuilder):
    def build_minutes(self, amount: int):
        self.tarrif.minutes = Minutes(amount)

    def build_internet(self, amount: int, speed: InternetSpeed):
        self.tarrif.internet = Internet(amount, speed)

    def build_messages(self, amount: int):
        self.tarrif.messages = Messages(amount)

    def build_add_ons(self, add_ons: dict[str, float]):
        self.tarrif.add_ons = [AddOn(n, p) for n, p in add_ons.items()]


## Изначально есть два тарифа: базовый и специальный
class BaseTarrif(TarrifBase):
    def total(self) -> float:
        return self.calculate_total(
            minutes=self.minutes,
            internet=self.internet,
            messages=self.messages,
            add_ons=self.add_ons,
            config=TarrifConfig(2, 6, 1),
        )


class BaseTarrifBuilder(TarrifBuilderBase):
    def reset(self):
        self.tarrif = BaseTarrif(
            minutes=Minutes(0),
            internet=Internet(0, speed=InternetSpeed.SLOW),
            messages=Messages(0),
            add_ons=[],
        )

    def get_tarrif(self) -> BaseTarrif:
        tarrif = self.tarrif
        self.reset()
        return tarrif


class SpecialTarrifValidationError(Exception):
    pass


class SpecialTarrif(TarrifBase):
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


class SpecialTarrifBuilder(TarrifBuilderBase):
    def reset(self):
        self.tarrif = SpecialTarrif(
            minutes=Minutes(350),
            internet=Internet(30, speed=InternetSpeed.MEDIUM),
            messages=Messages(100),
            add_ons=[],
        )

    def get_tarrif(self) -> BaseTarrif:
        if self.tarrif.minutes.amount < 350:
            raise SpecialTarrifValidationError(
                "Special Tarrif minutes amount can't be less than 350"
            )
        elif self.tarrif.internet.amount < 30:
            raise SpecialTarrifValidationError(
                "Special Tarrif internet amount can't be less than 30"
            )
        elif self.tarrif.internet.speed == InternetSpeed.SLOW:
            raise SpecialTarrifValidationError(
                "Special Tarrif internet speed can't be slow"
            )
        elif self.tarrif.messages.amount < 100:
            raise SpecialTarrifValidationError(
                "Special Tarrif messages amount can't be less than 100"
            )

        tarrif = self.tarrif
        self.reset()
        return tarrif


## Добавляем новый тариф без дополнений и с роумингом
class Roaming:
    def __init__(
        self,
        country: str,
        kf: float,
    ) -> None:
        self.country = country
        self.kf = kf


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
            config=TarrifConfig(2, 6, 1, roaming_kf=self.roaming.kf),
        )


class RoamingTarrifBuilder(TarrifBuilderBase):
    def build_roaming(self, country: str, kf: float):
        self.tarrif.roaming = Roaming(country, kf)

    def reset(self):
        self.tarrif = RoamingTarrif(
            minutes=Minutes(0),
            internet=Internet(0, speed=InternetSpeed.SLOW),
            messages=Messages(0),
            roaming=Roaming("RU", 1),
        )

    def get_tarrif(self) -> RoamingTarrif:
        tarrif = self.tarrif
        self.reset()
        return tarrif


def client_code():
    base_tarrif_builder = BaseTarrifBuilder()
    base_tarrif_builder.build_minutes(100)
    base_tarrif_builder.build_internet(15, InternetSpeed.MEDIUM)
    base_tarrif_builder.build_messages(50)
    base_tarrif_builder.build_add_ons({"Музкальный звонок": 50})
    base = base_tarrif_builder.get_tarrif()
    print(base.total())

    special_tarrif_builder = SpecialTarrifBuilder()
    special_tarrif_builder.build_minutes(350)
    special_tarrif_builder.build_internet(30, InternetSpeed.MEDIUM)
    special_tarrif_builder.build_messages(100)
    special_tarrif_builder.build_add_ons({"Музкальный звонок": 50})
    special = special_tarrif_builder.get_tarrif()
    print(special.total())

    roaming_tarrif_builder = RoamingTarrifBuilder()
    roaming_tarrif_builder.build_minutes(100)
    roaming_tarrif_builder.build_internet(10, InternetSpeed.MEDIUM)
    roaming_tarrif_builder.build_messages(50)
    roaming_tarrif_builder.build_roaming("US", 2)
    roaming = roaming_tarrif_builder.get_tarrif()
    print(roaming.total())


if __name__ == "__main__":
    client_code()
