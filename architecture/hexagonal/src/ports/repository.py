from abc import ABC
from abc import abstractmethod

from src.domain.task import Task
from src.domain.task import TaskList


class TaskRepositoryPort(ABC):
    @abstractmethod
    def get_task(self, id: str) -> Task:
        pass

    @abstractmethod
    def add_task(self, task: Task) -> str:
        pass

    @abstractmethod
    def get_task_list(self, id: str) -> TaskList:
        pass

    @abstractmethod
    def add_task_list(self, task_list: TaskList) -> str:
        pass

    @abstractmethod
    def add_task_to_list(self, task: Task, task_list: TaskList) -> None:
        pass
