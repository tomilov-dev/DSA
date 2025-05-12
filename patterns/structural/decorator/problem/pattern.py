"""
Решение задачи системы уведомлений через паттерн Декоратор
"""

from abc import ABC
from abc import abstractmethod
from pathlib import Path


## Копия наивной реализации


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


## Конец копии наивной реализации


class INotification(ABC):
    @abstractmethod
    def send(self, content: str, target: str) -> None:
        pass


class BaseNotification(INotification):
    def send(self, content: str, target: str) -> None:
        pass


class INotificationDecorator(INotification):
    def __init__(self, component: INotification) -> None:
        self._component = component

    @property
    def component(self) -> INotification:
        return self._component


class EmailNotificationDecorator(INotificationDecorator):
    def send_by_email(self, content: str, target: str) -> None:
        print(f"Send ''{content}'' to {target} through Email")

    def send(self, content: str, target: str) -> None:
        self.send_by_email(content, target)
        self.component.send(content, target)


class SMSNotificationDecorator(INotificationDecorator):
    def send_by_sms(self, content: str, target: str) -> None:
        print(f"Send '{content}' to {target} through SMS")

    def send(self, content: str, target: str) -> None:
        self.send_by_sms(content, target)
        self.component.send(content, target)


class PushNotificationDecorator(INotificationDecorator):
    def send_by_push(self, content: str, target: str) -> None:
        print(f"Send '{content}' to {target} through Push")

    def send(self, content: str, target: str) -> None:
        self.send_by_push(content, target)
        self.component.send(content, target)


class LogNotificationDecorator(INotificationDecorator):
    def __init__(
        self,
        component: INotification,
        logger: NotificationLogger,
    ) -> None:
        super().__init__(component)
        self.logger = logger

    def log(self, msg: str, content: str, target: str) -> None:
        self.logger.log(f"{msg} content: {content} to: {target}")

    def send(self, content: str, target: str) -> None:
        self.log("Start sending", content, target)
        self.component.send(content, target)
        self.log("End sending", content, target)


class CopyNotificationDecorator(INotificationDecorator):
    def __init__(
        self,
        component: INotification,
        copier: NotificationCopier,
    ) -> None:
        super().__init__(component)
        self.copier = copier

    def copy(self, content: str) -> None:
        self.copier.copy(content)

    def send(self, content: str, target: str) -> None:
        self.component.send(content, target)
        self.copy(content)


class NotificationFactory:
    @staticmethod
    def create_notification(
        logger: NotificationLogger,
        copier: NotificationCopier,
    ) -> INotification:
        notification = BaseNotification()
        notification = EmailNotificationDecorator(notification)
        notification = SMSNotificationDecorator(notification)
        notification = PushNotificationDecorator(notification)
        notification = LogNotificationDecorator(notification, logger)
        notification = CopyNotificationDecorator(notification, copier)
        return notification


def client_code():
    file_logger = FileLogger(Path("log_path.txt"))
    db_logger = DatabaseLogger("https://connection:9999")
    logger = NotificationLogger([file_logger, db_logger])

    file_copier = LocalCopier(Path("copy_path.txt"))
    network_copier = NetworkCopier("https://connection:9998")
    copier = NotificationCopier([file_copier, network_copier])

    notification = NotificationFactory.create_notification(logger, copier)
    notification.send("Hello, World!", "MySelf")


if __name__ == "__main__":
    client_code()
