import copy
from abc import ABC
from abc import abstractmethod


class Owner:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

    def __repr__(self) -> str:
        return f"{self.name}:{self.email}"


class ProjectComponent(ABC):
    def __init__(self, owner: Owner) -> None:
        self.owner = owner

    def __repr__(self) -> str:
        return str(self.owner)

    @abstractmethod
    def clone(self) -> "ProjectComponent":
        pass


class Task(ProjectComponent):
    def __init__(self, owner: Owner, title: str, description: str) -> None:
        super().__init__(owner)
        self.title = title
        self.description = description

    def clone(self) -> "Task":
        return copy.deepcopy(self)


class Subproject(ProjectComponent):
    def __init__(self, owner: Owner, name: str, tasks: list) -> None:
        super().__init__(owner)
        self.name = name
        self.tasks = tasks

    def clone(self) -> "Subproject":
        return copy.deepcopy(self)


def client_code():
    owner1 = Owner("John", "john@mail.ru")
    owner2 = Owner("Kris", "kris@mail.ru")

    task1 = Task(owner1, "Design Database", "Design the database schema")
    task2 = task1.clone()
    task2.owner = owner2
    task2.title = "Design Database Clone"

    print("Original Task:", task1)
    print("Cloned Task:", task2)

    subproject1 = Subproject(owner1, "Backend Development", [task1])
    subproject2 = subproject1.clone()
    subproject2.owner.email = "kris.clone@mail.ru"
    subproject2.name = "Backend Development Clone"
    subproject2.tasks[0].title = "Design Database Clone in Subproject"

    print("Original Subproject:", subproject1)
    print("Cloned Subproject:", subproject2)


if __name__ == "__main__":
    client_code()
