from abc import ABC
from abc import abstractmethod


class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message: str, recipient: str) -> None:
        pass


class EmailNotificationChannel(NotificationChannel):
    def send(self, message: str, recipient: str) -> None:
        print(f"Sending email to {recipient}: {message}")


class SMSNotificationChannel(NotificationChannel):
    def send(self, message: str, recipient: str) -> None:
        print(f"Sending SMS to {recipient}: {message}")


class PushNotificationChannel(NotificationChannel):
    def send(self, message: str, recipient: str) -> None:
        print(f"Sending push notification to {recipient}: {message}")


class Notification(ABC):
    def __init__(self, channel: NotificationChannel) -> None:
        self.channel = channel

    @abstractmethod
    def notify(self, message: str, recipient: str) -> None:
        pass


class EmailNotification(Notification):
    def notify(self, message: str, recipient: str) -> None:
        self.channel.send(message, recipient)


class SMSNotification(Notification):
    def notify(self, message: str, recipient: str) -> None:
        self.channel.send(message, recipient)


class PushNotification(Notification):
    def notify(self, message: str, recipient: str) -> None:
        self.channel.send(message, recipient)


def client_code():
    email_channel = EmailNotificationChannel()
    sms_channel = SMSNotificationChannel()
    push_channel = PushNotificationChannel()

    email_notification = EmailNotification(email_channel)
    sms_notification = SMSNotification(sms_channel)
    push_notification = PushNotification(push_channel)

    email_notification.notify("This is an email notification.", "user@example.com")
    sms_notification.notify("This is an SMS notification.", "+1234567890")
    push_notification.notify("This is a push notification.", "user_device_id")
