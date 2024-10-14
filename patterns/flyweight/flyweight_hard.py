from abc import ABC
from abc import abstractmethod
from typing import Type
from typing import TypeVar
from typing import Dict


T = TypeVar("T", bound="GameObject")


class GameObject(ABC):
    def __init__(
        self,
        name: str,
        texture: str,
        size: str,
    ) -> None:
        self.__name = name
        self.__texture = texture
        self.__size = size

    def display_data(self) -> str:
        return f"Name: {self.__name}, Texture: {self.__texture}, Size: {self.__size}"


class Tree(GameObject):
    pass


class Rock(GameObject):
    pass


class Building(GameObject):
    pass


class GameObjectFactory:
    def __init__(self) -> None:
        self._storage: Dict[tuple, GameObject] = dict()

    def get_object(self, type: Type[T], name: str, texture: str, size: str) -> T:
        key = (type, name, texture, size)
        if key not in self._storage:
            self._storage[key] = type(name, texture, size)
        return self._storage[key]  # type: ignore

    def get_tree(self, name: str, texture: str, size: str) -> Tree:
        return self.get_object(Tree, name, texture, size)

    def get_rock(self, name: str, texture: str, size: str) -> Rock:
        return self.get_object(Rock, name, texture, size)

    def get_building(self, name: str, texture: str, size: str) -> Building:
        return self.get_object(Building, name, texture, size)


class GameObjectContext:
    def __init__(
        self,
        object_data: GameObject,
        x: float,
        y: float,
    ) -> None:
        self.object_data = object_data
        self.x = x
        self.y = y

    def display(self) -> str:
        dp = self.object_data.display_data()
        return f"{dp} on ({self.x}, {self.y})"
