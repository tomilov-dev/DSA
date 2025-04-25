from datetime import datetime


class FlightBooking:
    def __init__(self) -> None:
        self._bid = 1
        self._booking = {}
        self._fligts: dict[tuple[str, str, datetime], int] = dict()

        self._fligts[("London", "Paris", datetime(2022, 1, 1))] = 1
        self._fligts[("Paris", "London", datetime(2022, 1, 1))] = 2

    def search_flights(
        self,
        source: str,
        destination: str,
        date: datetime,
    ) -> int | None:
        return self._fligts.get((source, destination, date))

    def book_flight(
        self,
        source: str,
        destination: str,
        date: datetime,
    ) -> int:
        self._booking[self._bid] = (source, destination, date)
        temp = self._bid
        self._bid += 1
        return temp

    def cancel_flight(
        self,
        flight_booking_id: int,
    ) -> str:
        self._booking[flight_booking_id] = None
        return f"Бронь {flight_booking_id} отменена"

    def get_flight_booking_status(
        self,
        flight_booking_id: int,
    ) -> str:
        if flight_booking_id not in self._booking:
            return "Бронь не найдена"

        status = self._booking.get(flight_booking_id)
        if status is None:
            return "Бронирование отменено"
        return "Забронировано"


class HotelBooking:
    def __init__(self) -> None:
        self._bid = 1
        self._booking = {}
        self._hotels: dict[tuple[str, datetime, datetime], int] = dict()

        self._hotels[("London", datetime(2022, 1, 1), datetime(2022, 1, 4))] = 1
        self._hotels[("Paris", datetime(2022, 1, 1), datetime(2022, 1, 4))] = 2

    def search_hotels(
        self,
        location: str,
        checkin: datetime,
        checkout: datetime,
    ) -> int | None:
        return self._hotels.get((location, checkin, checkout))

    def book_hotel(
        self,
        location: str,
        checkin: datetime,
        checkout: datetime,
    ) -> int:
        self._booking[self._bid] = (location, checkin, checkout)
        temp = self._bid
        self._bid += 1
        return temp

    def cancel_hotel(
        self,
        hotel_booking_id: str,
    ) -> str:
        self._booking[hotel_booking_id] = None
        return f"Бронь {hotel_booking_id} отменена"

    def get_hotel_booking_status(
        self,
        hotel_booking_id: str,
    ) -> str:
        if hotel_booking_id not in self._booking:
            return "Бронь не найдена"

        status = self._booking.get(hotel_booking_id)
        if status is None:
            return "Бронирование отменено"
        return "Забронировано"


class CarRental:
    def __init__(self) -> None:
        self._bid = 1
        self._booking = {}
        self._hotels: dict[tuple[str, datetime, datetime], int] = dict()

        self._hotels[("London", datetime(2022, 1, 1), datetime(2022, 1, 4))] = 1
        self._hotels[("Paris", datetime(2022, 1, 1), datetime(2022, 1, 4))] = 2

    def search_cars(
        self,
        location: str,
        pickup: datetime,
        dropoff: datetime,
    ) -> int | None:
        return self._hotels.get((location, pickup, dropoff))

    def book_car(
        self,
        location: str,
        pickup: datetime,
        dropoff: datetime,
    ) -> int:
        self._booking[self._bid] = (location, pickup, dropoff)
        temp = self._bid
        self._bid += 1
        return temp

    def cancel_car(
        self,
        car_booking_id: int,
    ) -> str:
        self._booking[car_booking_id] = None
        return f"Бронь {car_booking_id} отменена"

    def get_car_booking_status(
        self,
        car_booking_id: int,
    ) -> str:
        if car_booking_id not in self._booking:
            return "Бронь не найдена"

        status = self._booking.get(car_booking_id)
        if status is None:
            return "Бронирование отменено"
        return "Забронировано"


class PaymentProcessing:
    def __init__(self) -> None:
        self._pid = 1
        self._payments: dict[int, tuple[str, float, str, bool]] = {}

    def initiate_payment(
        self,
        person: str,
        amount: float,
        type: str,
    ) -> int:
        self._payments[self._pid] = (person, amount, type, True)
        temp = self._pid
        self._pid += 1
        return temp

    def get_payment_status(
        self,
        payment_id: int,
    ) -> bool | None:
        payment = self._payments.get(payment_id)
        if payment is None:
            return None
        return payment[3]

    def cancel_payment(
        self,
        payment_id: int,
    ) -> None:
        payment = self._payments.get(payment_id)
        if payment is not None:
            self._payments[payment_id] = (payment[0], payment[1], payment[2], False)


class TravelAgencyFacade:
    def __init__(
        self,
        flight_booking: FlightBooking,
        hotel_booking: HotelBooking,
        car_rental: CarRental,
        payment_processing: PaymentProcessing,
    ) -> None:
        self.flight_booking = flight_booking
        self.hotel_booking = hotel_booking
        self.cart_rental = car_rental
        self.payment_processing = payment_processing

    def search_flights(
        self,
        source: str,
        destination: str,
        date: datetime,
    ) -> int | None:
        return self.flight_booking.search_flights(source, destination, date)

    def book_flight(
        self,
        source: str,
        destination: str,
        date: datetime,
    ) -> int:
        return self.flight_booking.book_flight(source, destination, date)

    def cancel_flight(
        self,
        flight_booking_id: int,
    ) -> str:
        return self.flight_booking.cancel_flight(flight_booking_id)

    def get_flight_booking_status(
        self,
        flight_booking_id: int,
    ) -> str:
        return self.flight_booking.get_flight_booking_status(flight_booking_id)

    def search_hotels(
        self,
        location: str,
        checkin: datetime,
        checkout: datetime,
    ) -> int | None:
        return self.hotel_booking.search_hotels(location, checkin, checkout)

    def book_hotel(
        self,
        location: str,
        checkin: datetime,
        checkout: datetime,
    ) -> int:
        return self.hotel_booking.book_hotel(location, checkin, checkout)

    def cancel_hotel(
        self,
        hotel_booking_id: str,
    ) -> str:
        return self.hotel_booking.cancel_hotel(hotel_booking_id)

    def get_hotel_booking_status(
        self,
        hotel_booking_id: str,
    ) -> str:
        return self.hotel_booking.get_hotel_booking_status(hotel_booking_id)

    def search_cars(
        self,
        location: str,
        pickup: datetime,
        dropoff: datetime,
    ) -> int | None:
        return self.cart_rental.search_cars(location, pickup, dropoff)

    def book_car(
        self,
        location: str,
        pickup: datetime,
        dropoff: datetime,
    ) -> int:
        return self.cart_rental.book_car(location, pickup, dropoff)

    def cancel_car(
        self,
        car_booking_id: int,
    ) -> str:
        return self.cart_rental.cancel_car(car_booking_id)

    def get_car_booking_status(
        self,
        car_booking_id: int,
    ) -> str:
        return self.cart_rental.get_car_booking_status(car_booking_id)

    def initiate_payment(
        self,
        person: str,
        amount: float,
        type: str,
    ) -> int:
        return self.payment_processing.initiate_payment(person, amount, type)

    def get_payment_status(
        self,
        payment_id: int,
    ) -> bool | None:
        return self.payment_processing.get_payment_status(payment_id)

    def cancel_payment(
        self,
        payment_id: int,
    ) -> None:
        return self.payment_processing.cancel_payment(payment_id)
