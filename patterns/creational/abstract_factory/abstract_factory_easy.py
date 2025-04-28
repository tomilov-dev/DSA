from abc import ABC
from abc import abstractmethod


class Chair(ABC):
    @abstractmethod
    def sit_on(self) -> None:
        pass


class Sofa(ABC):
    @abstractmethod
    def sit_on(self) -> None:
        pass

    @abstractmethod
    def lay_on(self) -> None:
        pass


class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass


class ModernChair(Chair):
    def sit_on(self) -> None:
        print("Sit on ModernChair")


class ModernSofa(Sofa):
    def sit_on(self) -> None:
        print("Sit on ModernSofa")

    def lay_on(self) -> None:
        print("Lay on ModernSofa")


class VictorianChair(Chair):
    def sit_on(self) -> None:
        print("Sit on VictorianChair")


class VictorianSofa(Sofa):
    def sit_on(self) -> None:
        print("Sit on VictorianSofa")

    def lay_on(self) -> None:
        print("Lay on VictorianSofa")


class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()

    def create_sofa(self) -> Sofa:
        return ModernSofa()


class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_sofa(self) -> Sofa:
        return VictorianSofa()


def client_code(furniture_factory: FurnitureFactory) -> None:
    chair = furniture_factory.create_chair()
    sofa = furniture_factory.create_sofa()
    chair.sit_on()
    sofa.sit_on()
    sofa.lay_on()


if __name__ == "__main__":
    print("Client: Testing client code with the ModernFurnitureFactory:")
    client_code(ModernFurnitureFactory())
    print("\n")

    print("Client: Testing client code with the VictorianFurnitureFactory:")
    client_code(VictorianFurnitureFactory())
