from abc import ABC
from abc import abstractmethod


class UserProfile:
    def __init__(self) -> None:
        self.name: str | None = None
        self.age: int | None = None
        self.email: str | None = None
        self.address: str | None = None
        self.phone: str | None = None

    def set_name(self, name: str) -> None:
        self.name = name

    def set_age(self, age: int) -> None:
        self.age = age

    def set_email(self, email: str) -> None:
        self.email = email

    def set_address(self, address: str) -> None:
        self.address = address

    def set_phone(self, phone: str) -> None:
        self.phone = phone


class UserProfileBuilder(ABC):
    @abstractmethod
    def build_name(self, name: str) -> None:
        pass

    @abstractmethod
    def build_age(self, age: int) -> None:
        pass

    @abstractmethod
    def build_email(self, email: str) -> None:
        pass

    @abstractmethod
    def build_address(self, address: str) -> None:
        pass

    @abstractmethod
    def build_phone(self, phone: str) -> None:
        pass


class FaceBookProfileBuilder(UserProfileBuilder):
    def __init__(self) -> None:
        self.profile = UserProfile()

    def build_name(self, name: str) -> None:
        self.profile.set_name(name)

    def build_age(self, age: int) -> None:
        self.profile.set_age(age)

    def build_email(self, email: str) -> None:
        self.profile.set_email(email)

    def build_address(self, address: str) -> None:
        self.profile.set_address(address)

    def build_phone(self, phone: str) -> None:
        self.profile.set_phone(phone)

    def get_profile(self) -> UserProfile:
        return self.profile


class UserProfileDirector:
    def __init__(self, builder: UserProfileBuilder) -> None:
        self._builder = builder

    def construct_profile(
        self,
        name: str,
        age: int,
        email: str,
        address: str,
        phone: str,
    ) -> None:
        self._builder.build_name(name)
        self._builder.build_age(age)
        self._builder.build_email(email)
        self._builder.build_address(address)
        self._builder.build_phone(phone)
