from abc import ABC
from abc import abstractmethod

from pydantic import BaseModel

from src.task import TaskState


class TaskNotFound(Exception):
    pass


class TaskAlreadyExists(Exception):
    pass


class TaskDTO(BaseModel):
    id: str
    name: str
    state: TaskState
    subtasks: list["TaskDTO"]


class TaskListDTO(BaseModel):
    id: str
    name: str
    tasks: dict[str, TaskDTO]


class ITaskRepository(ABC):
    @abstractmethod
    def get_task(self, id: str) -> TaskDTO:
        pass

    @abstractmethod
    def add_task(self, task: TaskDTO) -> str:
        pass

    @abstractmethod
    def remove_task(self, task: TaskDTO) -> None:
        pass

    @abstractmethod
    def update_task(self, task: TaskDTO) -> None:
        pass

    @abstractmethod
    def get_task_list(self, id: str) -> TaskListDTO:
        pass

    @abstractmethod
    def add_task_list(self, task_list: TaskListDTO) -> str:
        pass

    @abstractmethod
    def add_task_to_list(self, task: TaskDTO, task_list: TaskListDTO) -> None:
        pass

    @abstractmethod
    def remove_task_from_list(self, task: TaskDTO, task_list: TaskListDTO) -> None:
        pass


class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self._tasks: dict[str, TaskDTO] = {}
        self._task_lists: dict[str, TaskListDTO] = {}

    def get_task(self, id: str) -> TaskDTO:
        if id not in self._tasks:
            raise TaskNotFound(f"Task with id {id} not found.")
        return self._tasks[id]

    def add_task(self, task: TaskDTO) -> str:
        if task.id in self._tasks:
            raise TaskAlreadyExists(f"Task with id {task.id} already exists.")
        self._tasks[task.id] = task
        return task.id

    def update_task(self, task: TaskDTO) -> None:
        self._tasks[task.id] = task

    def remove_task(self, task: TaskDTO) -> None:
        if task.id not in self._tasks:
            raise TaskNotFound(f"Task with id {task.id} not found.")
        for task_list in self._task_lists.values():
            if task.id in task_list.tasks:
                del task_list.tasks[task.id]
        del self._tasks[task.id]

    def get_task_list(self, id: str) -> TaskListDTO:
        if id not in self._task_lists:
            raise TaskNotFound(f"Task list with id {id} not found.")
        return self._task_lists[id]

    def add_task_list(self, task_list: TaskListDTO) -> str:
        if task_list.id in self._task_lists:
            raise TaskAlreadyExists(f"Task list with id {task_list.id} already exists.")
        self._task_lists[task_list.id] = task_list
        return task_list.id

    def add_task_to_list(self, task: TaskDTO, task_list: TaskListDTO) -> None:
        if task_list.id not in self._task_lists:
            raise TaskNotFound(f"Task List with id {task_list.id} not found.")
        self._task_lists[task_list.id].tasks[task.id] = task
        self._tasks[task.id] = task

    def remove_task_from_list(self, task: TaskDTO, task_list: TaskListDTO) -> None:
        if task_list.id not in self._task_lists:
            raise TaskNotFound(f"Task List with id {task_list.id} not found.")
        if task.id in self._task_lists[task_list.id].tasks:
            del self._task_lists[task_list.id].tasks[task.id]
