from uuid import uuid4

from src.task import Task
from src.task import TaskList
from src.task import TaskState
from src.repository import ITaskRepository


class TaskListService:
    def __init__(
        self,
        repository: ITaskRepository,
    ) -> None:
        self._repository = repository

    def add_task(
        self,
        name: str,
        state: str,
        subtasks: list[dict],
    ) -> str:
        task = Task(
            id=uuid4().hex,
            name=name,
            state=TaskState[state.upper()],
            subtasks=[
                Task(
                    id=uuid4().hex,
                    name=sub["name"],
                    state=TaskState[sub["state"].upper()],
                    subtasks=[],
                )
                for sub in subtasks
            ],
        )
        return self._repository.add_task(task)

    def add_task_list(
        self,
        name: str,
        tasks: list[dict],
    ) -> str:
        task_objs = [
            Task(
                id=uuid4().hex,
                name=t["name"],
                state=TaskState[t["state"].upper()],
                subtasks=[],
            )
            for t in tasks
        ]
        task_list = TaskList(id=uuid4().hex, name=name, tasks=task_objs)
        return self._repository.add_task_list(task_list)

    def add_task_to_list(
        self,
        task_id: str,
        task_list_id: str,
    ) -> None:
        task = self._repository.get_task(task_id)
        task_list = self._repository.get_task_list(task_list_id)
        self._repository.add_task_to_list(task, task_list)

    def get_task_list(
        self,
        task_list_id: str,
    ) -> TaskList:
        return self._repository.get_task_list(task_list_id)
