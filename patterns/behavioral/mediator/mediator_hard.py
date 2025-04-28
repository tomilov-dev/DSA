from abc import ABC, abstractmethod
from enum import Enum


class Event(Enum):
    REQUEST_TAKEOFF = "REQUEST_TAKEOFF"
    GRANT_TAKEOFF_PERMISSION = "GRANT_TAKEOFF_PERMISSION"
    REQUEST_REFUEL = "REQUEST_REFUEL"
    REQUEST_BOARDING = "REQUEST_BOARDING"
    FINISH_FLIGHT = "FINISH_FLIGHT"
    FLIGHT_STATUS_IN_TIME = "FLIGHT_STATUS_IN_TIME"
    FLIGHT_STATUS_CRUSH = "FLIGHT_STATUS_CRUSH"


class Mediator(ABC):
    @abstractmethod
    def register(self, actor: "Actor") -> None:
        pass

    @abstractmethod
    def notify(self, sender: "Actor", event: Event) -> None:
        pass


class FlightMediator(Mediator):
    def __init__(self) -> None:
        self.actors: list["Actor"] = []

    def register(self, actor: "Actor") -> None:
        self.actors.append(actor)

    def notify(self, sender: "Actor", event: Event) -> None:
        for actor in self.actors:
            if sender != actor:
                actor.receive_event(event)


class Actor(ABC):
    def __init__(self, mediator: Mediator) -> None:
        self.mediator = mediator
        self.mediator.register(self)

    @abstractmethod
    def send_event(self, event: Event) -> None:
        pass

    @abstractmethod
    def receive_event(self, event: Event) -> None:
        pass


class BaseActor(Actor):
    def send_event(self, event: Event) -> None:
        self.mediator.notify(self, event)


class Pilot(BaseActor):
    def receive_event(self, event: Event) -> None:
        if event == Event.GRANT_TAKEOFF_PERMISSION:
            print("Takeoff granted")

    def request_takeoff(self) -> None:
        self.send_event(Event.REQUEST_TAKEOFF)


class AirTrafficControl(BaseActor):
    def receive_event(self, event: Event) -> None:
        if event == Event.REQUEST_TAKEOFF:
            self.grant_takeoff_permission()
        elif event == Event.FINISH_FLIGHT:
            self.notify_flight_status()

    def grant_takeoff_permission(self) -> None:
        self.send_event(Event.GRANT_TAKEOFF_PERMISSION)

    def notify_flight_status(self) -> None:
        self.send_event(Event.FLIGHT_STATUS_IN_TIME)


class GroundCrew(BaseActor):
    def receive_event(self, event: Event) -> None:
        if event == Event.REQUEST_BOARDING:
            print("Boarding")
        elif event == Event.REQUEST_REFUEL:
            print("Refueling")

    def request_service(self) -> None:
        self.send_event(Event.REQUEST_REFUEL)


class Passenger(BaseActor):
    def receive_event(self, event: Event) -> None:
        if event == Event.FLIGHT_STATUS_IN_TIME:
            print("Clap clap")

    def request_boarding(self) -> None:
        self.send_event(Event.REQUEST_BOARDING)


# Пример использования
if __name__ == "__main__":
    mediator = FlightMediator()

    pilot = Pilot(mediator)
    atc = AirTrafficControl(mediator)
    ground_crew = GroundCrew(mediator)
    passenger = Passenger(mediator)

    # Симуляция действий
    pilot.request_takeoff()
    ground_crew.request_service()
    passenger.request_boarding()
    atc.notify_flight_status()
