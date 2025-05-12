"""
Решение задачи системы уведомлений (наивный подход)

Проблемы реализации:
- Сложность добавления функционала. Например, чтобы добавить шифрование уведомлений придется изменять существующий код.
- Отсутствие динамического расширения функционала. Нельзя "На лету" добавить или убрать функционал.
"""

from abc import ABC
from abc import abstractmethod
from pathlib import Path


class ILogger(ABC):
    @abstractmethod
    def log(self, msg: str) -> None:
        pass


class FileLogger(ILogger):
    def __init__(self, path: Path) -> None:
        self.path = path

    def log(self, msg: str) -> None:
        print(f"Logging '{msg}' with File Logger in {self.path}")


class DatabaseLogger(ILogger):
    def __init__(self, connection: str) -> None:
        self.connection = connection

    def log(self, msg: str) -> None:
        print(f"Logging '{msg}' with Database Logger")


class NotificationLogger:
    def __init__(self, engines: list[ILogger]):
        self.engines = engines

    def log(self, msg: str) -> None:
        for engine in self.engines:
            engine.log(msg)


class ICopier(ABC):
    @abstractmethod
    def copy(self, content: str) -> None:
        pass


class LocalCopier(ICopier):
    def __init__(self, path: Path) -> None:
        self.path = path

    def copy(self, content: str) -> None:
        print(f"Copy '{content}' with Local Copy in {self.path}")


class NetworkCopier(ICopier):
    def __init__(self, connection: str) -> None:
        self.connection = connection

    def copy(self, content: str) -> None:
        print(f"Copy '{content}' with Network Copy")


class NotificationCopier:
    def __init__(self, engines: list[ICopier]):
        self.engines = engines

    def copy(self, content: str) -> None:
        for engine in self.engines:
            engine.copy(content)


class INotificationEngine(ABC):
    def __init__(
        self,
        logger: NotificationLogger,
        copier: NotificationCopier,
        token: str,
    ) -> None:
        self.logger = logger
        self.copier = copier
        self.token = token

    @abstractmethod
    def send(self, content: str, target: str) -> None:
        pass


class EmailNotification(INotificationEngine):
    def send(self, content: str, target: str) -> None:
        self.logger.log("Start email notification")
        print(f"Send ''{content}'' to {target} through Email")
        self.copier.copy(content)
        self.logger.log("End email notification")


class SMSNotification(INotificationEngine):
    def send(self, content: str, target: str) -> None:
        self.logger.log("Start sms notification")
        print(f"Send '{content}' to {target} through SMS")
        self.copier.copy(content)
        self.logger.log("End sms notification")


class PushNotification(INotificationEngine):
    def send(self, content: str, target: str) -> None:
        self.logger.log("Start push notification")
        print(f"Send '{content}' to {target} through Push")
        self.copier.copy(content)
        self.logger.log("End push notification")


class Notification:
    def __init__(self, engines: list[INotificationEngine]) -> None:
        self.engines = engines

    def send(self, content: str, target: str) -> None:
        for engine in self.engines:
            engine.send(content, target)


def client_code():
    file_logger = FileLogger(Path("log_path.txt"))
    db_logger = DatabaseLogger("https://connection:9999")
    logger = NotificationLogger([file_logger, db_logger])

    file_copier = LocalCopier(Path("copy_path.txt"))
    network_copier = NetworkCopier("https://connection:9998")
    copier = NotificationCopier([file_copier, network_copier])

    email = EmailNotification(logger, copier, "email_token")
    sms = SMSNotification(logger, copier, "sms_token")
    push = PushNotification(logger, copier, "push_token")

    notification = Notification([email, sms, push])
    notification.send("Hello, World!", "MySelf")


if __name__ == "__main__":
    client_code()
