from abc import ABC
from abc import abstractmethod
from typing import Any

from src.task import ITask
from src.task import ITaskList
from src.task import Task
from src.task import TaskList
from src.repository import TaskDTO
from src.repository import TaskListDTO
from src.repository import ITaskRepository
from src.task import ITaskFactory
from src.task import ITaskListFactory


class ITaskDTOAdapter(ABC):
    @abstractmethod
    def to_dto(self, task: ITask) -> TaskDTO:
        pass

    @abstractmethod
    def from_dto(self, dto: TaskDTO) -> ITask:
        pass


class TaskDTOAdapter(ITaskDTOAdapter):
    def to_dto(self, task: ITask) -> TaskDTO:
        return TaskDTO(
            id=task.id,
            name=task.name,
            state=task.state,
            subtasks=[self.to_dto(subtask) for subtask in task.subtasks],
        )

    def from_dto(self, dto: TaskDTO) -> ITask:
        return Task(
            id=dto.id,
            name=dto.name,
            state=dto.state,
            subtasks=[self.from_dto(sub_dto) for sub_dto in dto.subtasks],
        )


class ITaskListDTOAdapter(ABC):
    def __init__(self, task_adapter: ITaskDTOAdapter):
        self._task_adapter = task_adapter

    @abstractmethod
    def to_dto(self, task_list: ITaskList) -> TaskListDTO:
        pass

    @abstractmethod
    def from_dto(self, dto: TaskListDTO) -> ITaskList:
        pass


class TaskListDTOAdapter(ITaskListDTOAdapter):
    def to_dto(self, task_list: ITaskList) -> TaskListDTO:
        return TaskListDTO(
            id=task_list.id,
            name=task_list.name,
            tasks={
                task.id: self._task_adapter.to_dto(task) for task in task_list.tasks
            },
        )

    def from_dto(self, dto: TaskListDTO) -> ITaskList:
        return TaskList(
            id=dto.id,
            name=dto.name,
            tasks=[self._task_adapter.from_dto(task) for task in dto.tasks.values()],
        )


class ITaskListService(ABC):
    def __init__(
        self,
        repository: ITaskRepository,
        task_factory: ITaskFactory,
        task_list_factory: ITaskListFactory,
        task_adapter: ITaskDTOAdapter,
        task_list_adapter: ITaskListDTOAdapter,
    ):
        self._repository = repository
        self._task_factory = task_factory
        self._task_list_factory = task_list_factory
        self._task_adapter = task_adapter
        self._task_list_adapter = task_list_adapter

    @abstractmethod
    def add_task(
        self,
        name: str,
        state: str,
        subtasks: list[dict[str, Any]],
    ) -> str:
        pass

    @abstractmethod
    def add_task_list(
        self,
        name: str,
        tasks: list[dict[str, Any]],
    ) -> str:
        pass

    @abstractmethod
    def add_task_to_list(
        self,
        task_id: str,
        task_list_id: str,
    ) -> None:
        pass

    @abstractmethod
    def get_task_list(self, task_list_id: str) -> TaskListDTO:
        pass


class TaskListService(ITaskListService):
    def add_task(
        self,
        name: str,
        state: str,
        subtasks: list[dict[str, Any]],
    ) -> str:
        subtask_objs = [
            self._task_factory.create(sub["name"], sub["state"], []) for sub in subtasks
        ]
        task = self._task_factory.create(name, state, subtask_objs)
        task_dto = self._task_adapter.to_dto(task)
        return self._repository.add_task(task_dto)

    def add_task_list(
        self,
        name: str,
        tasks: list[dict[str, Any]],
    ) -> str:
        task_objs = [
            self._task_factory.create(t["name"], t["state"], []) for t in tasks
        ]
        task_list = self._task_list_factory.create(name, task_objs)
        task_list_dto = self._task_list_adapter.to_dto(task_list)
        return self._repository.add_task_list(task_list_dto)

    def add_task_to_list(
        self,
        task_id: str,
        task_list_id: str,
    ) -> None:
        task_dto = self._repository.get_task(task_id)
        task_list_dto = self._repository.get_task_list(task_list_id)
        self._repository.add_task_to_list(task_dto, task_list_dto)

    def get_task_list(self, task_list_id: str) -> TaskListDTO:
        task_list_dto = self._repository.get_task_list(task_list_id)
        return task_list_dto
