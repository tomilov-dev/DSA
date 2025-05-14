"""
Решение задачи обработчика HTTP-запроса (наивный подход)

Проблемы реализации:
1. Жесткая структура - для изменения обработки нужно менять или создавать новый RequestHandler
2. Нет динамической конфигурации - нельзя собрать обработчик "на лету"
3. Сложнее переиспользовать обработчики
"""

import re
from abc import ABC
from abc import abstractmethod
from typing import Any


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
    @abstractmethod
    def handle(self, request: Request) -> Any:
        pass


class AuthenticationHandler(IRequestHandler):
    def __init__(self, tokens: dict[str, bool]) -> None:
        self.tokens = tokens

    def handle(self, request: Request) -> None:
        if request.token not in self.tokens:
            raise AuthenticationError(f"Requset {request.id} has wrong token")


class AuthorizationHandler(IRequestHandler):
    def __init__(self, tokens: dict[str, bool]) -> None:
        self.tokens = tokens

    def handle(self, request: Request) -> None:
        if not self.tokens.get(request.token, False):
            raise AuthorizationError(f"Request {request.id} has no permission")


class ValidationHandler(IRequestHandler):
    def handle(self, request: Request) -> None:
        if isinstance(request.data, int):
            return None
        elif isinstance(request.data, str) and VALIDATION_RX.match(request.data):
            return None
        raise ValidationError(f"Request {request.id} has not valid data")


class LogHandler(IRequestHandler):
    def handle(self, request: Request) -> None:
        print(f"Log request <{request.id}>")


class ResponseHandler(IRequestHandler):
    def handle(self, request: Request) -> int:
        return int(request.data) * 2


class DefaultRequestHandler(IRequestHandler):
    def __init__(
        self,
        authentication: IRequestHandler,
        authorization: IRequestHandler,
        validation: IRequestHandler,
        logger: IRequestHandler,
        response_handler: IRequestHandler,
    ) -> None:
        self.authentication = authentication
        self.authorization = authorization
        self.validation = validation
        self.logger = logger
        self.response_handler = response_handler

    def handle(self, request: Request) -> int:
        self.authentication.handle(request)
        self.authorization.handle(request)
        self.validation.handle(request)
        self.logger.handle(request)
        return self.response_handler.handle(request)


def client_code():
    tokens = {"token1": True, "token2": False}

    authentication = AuthenticationHandler(tokens)
    authorization = AuthorizationHandler(tokens)
    validation = ValidationHandler()
    logger = LogHandler()
    response_handler = ResponseHandler()

    request_handler = DefaultRequestHandler(
        authentication,
        authorization,
        validation,
        logger,
        response_handler,
    )

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
