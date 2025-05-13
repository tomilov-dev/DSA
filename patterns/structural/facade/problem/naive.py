"""
Решение задачи системы онлайн-заказов билетов в кинотеатр (наивный подход)

Текущие проблемы:
1. Клиентский код знает от всех сервисах. Если что-то изменится в одном из сервисов, это может повлечь изменения в клиентском коде.
2. Дублирование кода. Потенциально возможно ситуация, когда оформление билета будет использоваться в нескольких местах.
3. Сложность масштабирования. Дополнительная операция приведет к необходимости менять клиентский код.
4. Нарушение ORP-приница (единой ответственности). Клиентский код отвечает и за бизнес-логику, и за работу с сервисами.
"""

import random


SEED = 1999


class InvalidBooking(Exception):
    pass


class HallService:
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


class BookingService:
    def book(self, hall: int, row: int, line: int) -> int:
        print("Seat is booked. Proccess the payment.")
        return hall * 10000 + row + line


class PaymentService:
    def pay(self, ticket: int) -> str:
        print("Ticket is payed.")
        return f"Payed ticket info {ticket}"


class NotificationService:
    def notify(self, ticket: int) -> None:
        print(f"Seat booked and payed. Follow the instructions on your ticket {ticket}")


def client_code(hall: int, row: int, line: int):
    halls = HallService()
    booking = BookingService()
    payment = PaymentService()
    notification = NotificationService()
    if not halls.check_seat(hall, row, line):
        return None

    ticket = booking.book(hall, row, line)
    payment.pay(ticket)
    notification.notify(ticket)


if __name__ == "__main__":
    client_code(1, 2, 3)
