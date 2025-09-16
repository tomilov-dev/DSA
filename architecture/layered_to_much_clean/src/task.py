from abc import ABC
from abc import abstractmethod
from collections.abc import Sequence
from enum import Enum
from uuid import uuid4


class InvalidTaskState(Exception):
    pass


class TaskStateError(Exception):
    pass


class TaskState(str, Enum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"


class ITask(ABC):
    def __init__(
        self,
        id: str,
        name: str,
        state: TaskState,
        subtasks: Sequence["ITask"],
    ) -> None:
        self._id = id
        self._name = name
        self._state = state
        self._subtasks = subtasks

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def state(self) -> TaskState:
        return self._state

    @property
    def subtasks(self) -> Sequence["ITask"]:
        return self._subtasks

    @abstractmethod
    def subtasks_completed(self) -> bool:
        pass

    @abstractmethod
    def complete(self) -> None:
        pass

    @abstractmethod
    def completed(self) -> bool:
        pass

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


class ITaskFactory(ABC):
    @abstractmethod
    def create(
        self,
        name: str,
        state: str,
        subtasks: Sequence[ITask],
    ) -> ITask:
        pass


class Task(ITask):
    def subtasks_completed(self) -> bool:
        for sub_task in self._subtasks:
            if sub_task._state != TaskState.COMPLETED:
                return False
        return True

    def complete(self) -> None:
        if not self.subtasks_completed():
            raise TaskStateError("Cannot complete task with incomplete subtasks.")
        self._state = TaskState.COMPLETED

    def completed(self) -> bool:
        return self._state == TaskState.COMPLETED and self.subtasks_completed()


class TaskFactory(ITaskFactory):
    def create(
        self,
        name: str,
        state: str,
        subtasks: Sequence[ITask],
    ) -> ITask:
        id = uuid4().hex
        if state not in TaskState.__members__:
            raise InvalidTaskState(
                f"Invalid state: {state}. Allowed: {list(TaskState.__members__.keys())}"
            )
        return Task(id, name, TaskState[state], subtasks)


class ITaskList(ABC):
    def __init__(
        self,
        id: str,
        name: str,
        tasks: Sequence[ITask],
    ) -> None:
        self._id = id
        self._name = name
        self._tasks = tasks

    @property
    def id(self) -> str:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def tasks(self) -> Sequence[ITask]:
        return self._tasks

    @abstractmethod
    def complete(self, task: ITask) -> None:
        pass


class ITaskListFactory(ABC):
    @abstractmethod
    def create(
        self,
        name: str,
        tasks: Sequence[ITask],
    ) -> ITaskList:
        pass


class TaskList(ITaskList):
    def complete(self, task: ITask) -> None:
        task.complete()

    def __str__(self) -> str:
        return (
            f"TaskList(id={self.id}, name={self.name}, "
            f"tasks=[{', '.join(str(task) for task in self.tasks)}])"
        )

    def __repr__(self) -> str:
        return f"TaskList(id={self.id!r}, name={self.name!r}, tasks={self.tasks!r})"


class TaskListFactory(ITaskListFactory):
    def create(
        self,
        name: str,
        tasks: Sequence[ITask],
    ) -> ITaskList:
        id = uuid4().hex
        return TaskList(id, name, tasks)
