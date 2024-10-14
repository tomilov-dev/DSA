from abc import ABC
from abc import abstractmethod


class UserService(ABC):
    @abstractmethod
    def get_user_info(self, user_id: str) -> dict:
        pass


class OldUserService(UserService):
    def get_user_info(self, user_id: str) -> dict:
        return {"user_name": "Ivan"}


class NewUserService:
    def fetch_user(self, user_id: str) -> dict:
        return {"username": "Ivan"}


class UserServiceAdapter(UserService):
    def __init__(
        self,
        new_user_service: NewUserService,
    ) -> None:
        self.new_user_service = new_user_service

    def get_user_info(self, user_id: str) -> dict:
        return {"user_name": self.new_user_service.fetch_user(user_id)["username"]}


def client_code():
    old_service = OldUserService()
    new_service = UserServiceAdapter(NewUserService())

    user_id = "12345"
    print(f"User info (old service): {old_service.get_user_info(user_id)}")
    print(f"User info (new service): {new_service.get_user_info(user_id)}")
