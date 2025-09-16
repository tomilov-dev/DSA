from abc import ABC
from abc import abstractmethod

from src.task import Task
from src.task import TaskList


class TaskNotFound(Exception):
    pass


class TaskAlreadyExists(Exception):
    pass


class ITaskRepository(ABC):
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


class InMemoryTaskRepository(ITaskRepository):
    def __init__(self):
        self._tasks: dict[str, Task] = {}
        self._task_lists: dict[str, TaskList] = {}

    def get_task(self, id: str) -> Task:
        if id not in self._tasks:
            raise TaskNotFound(f"Task with id {id} not found.")
        return self._tasks[id]

    def add_task(self, task: Task) -> str:
        if task.id in self._tasks:
            raise TaskAlreadyExists(f"Task with id {task.id} already exists.")
        self._tasks[task.id] = task
        return task.id

    def get_task_list(self, id: str) -> TaskList:
        if id not in self._task_lists:
            raise TaskNotFound(f"Task list with id {id} not found.")
        return self._task_lists[id]

    def add_task_list(self, task_list: TaskList) -> str:
        if task_list.id in self._task_lists:
            raise TaskAlreadyExists(f"Task list with id {task_list.id} already exists.")
        self._task_lists[task_list.id] = task_list
        return task_list.id

    def add_task_to_list(self, task: Task, task_list: TaskList) -> None:
        if task_list.id not in self._task_lists:
            raise TaskNotFound(f"Task List with id {task_list.id} not found.")
        self._task_lists[task_list.id].tasks.append(task)
        self._tasks[task.id] = task
