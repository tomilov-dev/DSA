from enum import Enum


class TaskStateError(Exception):
    pass


class TaskState(str, Enum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"


class Task:
    def __init__(self, id: str, name: str, state: TaskState, subtasks: list["Task"]):
        self.id = id
        self.name = name
        self.state = state
        self.subtasks = subtasks

    def subtasks_completed(self) -> bool:
        return all(sub.state == TaskState.COMPLETED for sub in self.subtasks)

    def complete(self) -> None:
        if not self.subtasks_completed():
            raise TaskStateError("Cannot complete task with incomplete subtasks.")
        self._state = TaskState.COMPLETED

    def completed(self) -> bool:
        return self.state == TaskState.COMPLETED and self.subtasks_completed()

    def __str__(self) -> str:
        return (
            f"Task(id={self.id}, name={self.name}, state={self.state}, "
            f"subtasks=[{', '.join(str(sub) for sub in self.subtasks)}])"
        )

    def __repr__(self) -> str:
        return (
            f"Task(id={self.id!r}, name={self.name!r}, state={self.state!r}, "
            f"subtasks={self.subtasks!r})"
        )


class TaskList:
    def __init__(self, id: str, name: str, tasks: list[Task]):
        self.id = id
        self.name = name
        self.tasks = tasks

    def complete(self, task: Task) -> None:
        task.complete()

    def __str__(self) -> str:
        return (
            f"TaskList(id={self.id}, name={self.name}, "
            f"tasks=[{', '.join(str(task) for task in self.tasks)}])"
        )

    def __repr__(self) -> str:
        return f"TaskList(id={self.id!r}, name={self.name!r}, tasks={self.tasks!r})"
