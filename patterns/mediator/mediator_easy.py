from abc import ABC, abstractmethod


class IDevice(ABC):
    def __init__(self, mediator: "Mediator") -> None:
        self.mediator = mediator
        self.register()

    @abstractmethod
    def register(self) -> None:
        pass

    @abstractmethod
    def send_event(self, event: str) -> None:
        pass

    @abstractmethod
    def receive_event(self, event: str) -> None:
        pass


class Light(IDevice):
    def turn_on(self) -> None:
        print("Включение света")
        self.send_event("light_on")

    def turn_off(self) -> None:
        print("Выключение света")
        self.send_event("light_off")

    def register(self) -> None:
        self.mediator.register_device("light", self)

    def send_event(self, event: str) -> None:
        self.mediator.notify(self, event)

    def receive_event(self, event: str) -> None:
        if event == "motion_detected":
            self.turn_on()


class Thermostat(IDevice):
    def raise_temperature(self):
        print("Повышение температуры")
        self.send_event("temperature_raised")

    def lower_temperature(self):
        print("Понижение температуры")
        self.send_event("temperature_lowered")

    def register(self) -> None:
        self.mediator.register_device("therm", self)

    def send_event(self, event: str) -> None:
        self.mediator.notify(self, event)

    def receive_event(self, event: str) -> None:
        if event == "temperature_drop":
            self.raise_temperature()


class Alarm(IDevice):
    def turn_on(self) -> None:
        print("Включение сигнализации")
        self.send_event("alarm_on")

    def turn_off(self) -> None:
        print("Выключение сигнализации")
        self.send_event("alarm_off")

    def register(self) -> None:
        self.mediator.register_device("alarm", self)

    def send_event(self, event: str) -> None:
        self.mediator.notify(self, event)

    def receive_event(self, event: str) -> None:
        if event == "intrusion_detected":
            self.turn_on()


class Mediator(ABC):
    def __init__(self) -> None:
        self.devices: dict[str, IDevice] = dict()

    @abstractmethod
    def register_device(self, device_name: str, device: IDevice) -> None:
        pass

    @abstractmethod
    def notify(self, sender: IDevice, event: str) -> None:
        pass


class HomeMediator(Mediator):
    def register_device(self, device_name: str, device: IDevice) -> None:
        self.devices[device_name] = device

    def notify(self, sender: IDevice, event: str) -> None:
        for device_name, device in self.devices.items():
            if device != sender:
                device.receive_event(event)


def client_code():
    mediator = HomeMediator()

    light = Light(mediator)
    thermostat = Thermostat(mediator)
    alarm = Alarm(mediator)

    light.send_event("motion_detected")
    thermostat.send_event("temperature_drop")
    alarm.send_event("intrusion_detected")

    light.turn_on()
    thermostat.raise_temperature()
    alarm.turn_on()
