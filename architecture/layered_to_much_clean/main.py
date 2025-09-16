from src.service import TaskListService
from src.repository import InMemoryTaskRepository

from src.task import TaskFactory
from src.task import TaskListFactory

from src.service import TaskDTOAdapter
from src.service import TaskListDTOAdapter


if __name__ == "__main__":
    repository = InMemoryTaskRepository()
    task_factory = TaskFactory()
    task_adapter = TaskDTOAdapter()
    task_list_factory = TaskListFactory()
    task_list_adapter = TaskListDTOAdapter(task_adapter)
    service = TaskListService(
        repository=repository,
        task_factory=task_factory,
        task_adapter=task_adapter,
        task_list_factory=task_list_factory,
        task_list_adapter=task_list_adapter,
    )

    task_id = service.add_task(name="Example Task", state="IN_PROGRESS", subtasks=[])
    task_list_id = service.add_task_list(name="Example Task List", tasks=[])

    service.add_task_to_list(task_id=task_id, task_list_id=task_list_id)
    task_list_dto = service.get_task_list(task_list_id=task_list_id)

    print(task_list_dto)
