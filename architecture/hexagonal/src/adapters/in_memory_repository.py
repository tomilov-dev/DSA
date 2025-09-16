from src.ports.repository import TaskRepositoryPort
from src.domain.task import Task, TaskList


class InMemoryTaskRepository(TaskRepositoryPort):
    def __init__(self):
        self._tasks: dict[str, Task] = {}
        self._task_lists: dict[str, TaskList] = {}

    def get_task(self, id: str) -> Task:
        return self._tasks[id]

    def add_task(self, task: Task) -> str:
        self._tasks[task.id] = task
        return task.id

    def get_task_list(self, id: str) -> TaskList:
        return self._task_lists[id]

    def add_task_list(self, task_list: TaskList) -> str:
        self._task_lists[task_list.id] = task_list
        return task_list.id

    def add_task_to_list(self, task: Task, task_list: TaskList) -> None:
        self._task_lists[task_list.id].tasks.append(task)
        self._tasks[task.id] = task
