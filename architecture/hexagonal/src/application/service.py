from uuid import uuid4

from src.domain.task import Task
from src.domain.task import TaskList
from src.domain.task import TaskState
from src.ports.repository import TaskRepositoryPort


class TaskListService:
    def __init__(self, repository: TaskRepositoryPort):
        self._repository = repository

    def add_task(self, name: str, state: str, subtasks: list[dict]) -> str:
        subtask_objs = [
            Task(uuid4().hex, sub["name"], TaskState[sub["state"]], [])
            for sub in subtasks
        ]
        task = Task(uuid4().hex, name, TaskState[state], subtask_objs)
        return self._repository.add_task(task)

    def add_task_list(self, name: str, tasks: list[dict]) -> str:
        task_objs = [
            Task(uuid4().hex, t["name"], TaskState[t["state"]], []) for t in tasks
        ]
        task_list = TaskList(uuid4().hex, name, task_objs)
        return self._repository.add_task_list(task_list)

    def add_task_to_list(self, task_id: str, task_list_id: str) -> None:
        task = self._repository.get_task(task_id)
        task_list = self._repository.get_task_list(task_list_id)
        self._repository.add_task_to_list(task, task_list)

    def get_task_list(self, task_list_id: str) -> TaskList:
        return self._repository.get_task_list(task_list_id)
