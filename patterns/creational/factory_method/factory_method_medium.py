from abc import ABC
from abc import abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self) -> None:
        pass

    @abstractmethod
    def stop_engine(self) -> None:
        pass


class VehicleCreator(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass

    def manage_vehicle(self, vehicle: Vehicle):
        vehicle.start_engine()
        vehicle.stop_engine()


class Car(Vehicle):
    def start_engine(self) -> None:
        print("Car engine started")

    def stop_engine(self) -> None:
        print("Car engine stopped")


class Truck(Vehicle):
    def start_engine(self) -> None:
        print("Truck engine started")

    def stop_engine(self) -> None:
        print("Truck engine stopped")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        print("Motorcycle engine started")

    def stop_engine(self) -> None:
        print("Motorcycle engine stopped")


class CarCreator(VehicleCreator):
    def create_vehicle(self) -> Vehicle:
        return Car()


class TruckCreator(VehicleCreator):
    def create_vehicle(self) -> Vehicle:
        return Truck()


class MotorcycleCreator(VehicleCreator):
    def create_vehicle(self) -> Vehicle:
        return Motorcycle()


def client_code(creator: VehicleCreator) -> None:
    vehicle = creator.create_vehicle()
    creator.manage_vehicle(vehicle)


if __name__ == "__main__":
    print("App: Launched with the CarCreator.")
    client_code(CarCreator())
    print("\n")

    print("App: Launched with the TruckCreator.")
    client_code(TruckCreator())
    print("\n")

    print("App: Launched with the MotorcycleCreator.")
    client_code(MotorcycleCreator())
