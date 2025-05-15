"""
Решение задачи обработчика HTTP-запроса через паттерн Цепочки обязанностей
"""

import re
from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Union


class Request:
    def __init__(
        self,
        id: int,
        token: str,
        data: int | str,
    ) -> None:
        self.id = id
        self.token = token
        self.data = data


VALIDATION_RX = re.compile(r"^\d+$")


class AuthenticationError(Exception):
    pass


class AuthorizationError(Exception):
    pass


class ValidationError(Exception):
    pass


class IRequestHandler(ABC):
    def __init__(
        self,
        next_handler: Union["IRequestHandler", None] = None,
    ) -> None:
        self._next_handler = next_handler

    @abstractmethod
    def handle(self, request: Request) -> Any:
        pass

    @abstractmethod
    def next(self, request: Request) -> Any:
        pass

    @abstractmethod
    def set_next(self, handler: "IRequestHandler") -> "IRequestHandler":
        pass


class BaseHandler(IRequestHandler):
    def set_next(self, handler: IRequestHandler) -> IRequestHandler:
        self._next_handler = handler
        return handler

    def next(self, request: Request) -> Any:
        if self._next_handler:
            return self._next_handler.handle(request)


class AuthenticationHandler(BaseHandler):
    def __init__(
        self,
        next_handler: IRequestHandler | None = None,
        tokens: dict[str, bool] | None = None,
    ) -> None:
        super().__init__(next_handler)
        self.tokens = tokens

    def handle(self, request: Request) -> Any:
        if self.tokens and request.token not in self.tokens:
            raise AuthenticationError(f"Requset {request.id} has wrong token")
        return self.next(request)


class AuthorizationHandler(BaseHandler):
    def __init__(
        self,
        next_handler: IRequestHandler | None = None,
        tokens: dict[str, bool] | None = None,
    ) -> None:
        super().__init__(next_handler)
        self.tokens = tokens

    def handle(self, request: Request) -> Any:
        if self.tokens and not self.tokens.get(request.token, False):
            raise AuthorizationError(f"Request {request.id} has not permission")
        return self.next(request)


class ValidationHandler(BaseHandler):
    def handle(self, request: Request) -> Any:
        if isinstance(request.data, int):
            return self.next(request)
        if isinstance(request.data, str) and VALIDATION_RX.match(request.data):
            return self.next(request)
        raise ValidationError(f"Request {request.id} has not valid data")


class LogHandler(BaseHandler):
    def handle(self, request: Request) -> Any:
        print(f"Log request <{request.id}>")
        return self.next(request)


class ResponseHandler(BaseHandler):
    def handle(self, request: Request) -> int:
        return int(request.data) * 2


def client_code():
    tokens = {"token1": True, "token2": False}

    response_handler = ResponseHandler()
    logger = LogHandler(response_handler)
    validation = ValidationHandler(logger)
    authorization = AuthorizationHandler(validation, tokens)
    authentication = AuthenticationHandler(authorization, tokens)
    request_handler = authentication

    requests = [
        Request(1, "token1", 123),
        Request(2, "token1", "abc"),
        Request(3, "token2", "123"),
        Request(4, "token3", "153"),
    ]
    for request in requests:
        try:
            response = request_handler.handle(request)
            print("Response is:", response)

        except Exception as ex:
            print(ex)


if __name__ == "__main__":
    client_code()
