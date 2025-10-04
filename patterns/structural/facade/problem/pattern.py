"""
Решение задачи системы онлайн-заказов билетов в кинотеатр через паттерн Фасад
"""

import random
from abc import ABC
from abc import abstractmethod

SEED = 1999


## SAME CODE STARTS


class InvalidBooking(Exception):
    pass


class IHallService(ABC):
    @abstractmethod
    def free_seats(self, hall: int) -> list[list[int]]:
        pass

    @abstractmethod
    def is_free_seat(self, hall: int, row: int, line: int) -> bool:
        pass

    @abstractmethod
    def check_seat(self, hall: int, row: int, line: int) -> bool:
        pass


class HallService(IHallService):
    def free_seats(self, hall: int) -> list[list[int]]:
        random.seed(hall)
        max_line = random.randint(7, 15)
        max_row = random.randint(3, 10)
        seats = [[random.randint(0, max_line)] for _ in range(max_row)]
        random.seed(SEED)
        return seats

    def is_free_seat(self, hall: int, row: int, line: int) -> bool:
        random.seed(hall * row * line)
        is_free = random.random() >= 0.5
        random.seed(SEED)
        return is_free

    def check_seat(self, hall: int, row: int, line: int) -> bool:
        if not self.is_free_seat(hall, row, line):
            free = self.free_seats(hall)
            print(
                f"Seat {row} {line} in hall {hall} is booked. Check other free seat: {free}"
            )
            return False
        print(f"Seat {row} {line} in hall {hall} is free")
        return True


class IBookingService(ABC):
    @abstractmethod
    def book(self, hall: int, row: int, line: int) -> int:
        pass


class BookingService(IBookingService):
    def book(self, hall: int, row: int, line: int) -> int:
        print("Seat is booked. Proccess the payment.")
        return hall * 10000 + row + line


class IPaymentService(ABC):
    @abstractmethod
    def pay(self, ticket: int) -> str:
        pass


class PaymentService(IPaymentService):
    def pay(self, ticket: int) -> str:
        print("Ticket is payed.")
        return f"Payed ticket info {ticket}"


class INotificationService:
    @abstractmethod
    def notify(self, ticket: int) -> None:
        pass


class NotificationService(INotificationService):
    def notify(self, ticket: int) -> None:
        print(f"Seat booked and payed. Follow the instructions on your ticket {ticket}")


## SAME CODE ENDS


class IOrderFacade(ABC):
    def __init__(
        self,
        hall_service: IHallService,
        booking_service: IBookingService,
        payment_service: IPaymentService,
        notification_service: INotificationService,
    ) -> None:
        self.hall_service = hall_service
        self.booking_service = booking_service
        self.payment_serivce = payment_service
        self.notification_service = notification_service

    @abstractmethod
    def order(self, hall: int, row: int, line: int) -> str:
        pass


class OrderFacade(IOrderFacade):
    def order(self, hall: int, row: int, line: int) -> str:
        if not self.hall_service.check_seat(hall, row, line):
            raise InvalidBooking(f"Seat {row} {line} in hall {hall} is booked.")

        ticket = self.booking_service.book(hall, row, line)
        ticket_info = self.payment_serivce.pay(ticket)
        self.notification_service.notify(ticket)
        return ticket_info


def client_code(hall: int, row: int, line: int):
    halls = HallService()
    booking = BookingService()
    payment = PaymentService()
    notification = NotificationService()
    order_facade = OrderFacade(
        hall_service=halls,
        booking_service=booking,
        payment_service=payment,
        notification_service=notification,
    )

    order_facade.order(hall, row, line)


if __name__ == "__main__":
    client_code(1, 2, 3)
