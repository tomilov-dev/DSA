from src.application.service import TaskListService
from src.adapters.in_memory_repository import InMemoryTaskRepository


if __name__ == "__main__":
    repository = InMemoryTaskRepository()
    service = TaskListService(repository)

    task_id = service.add_task(name="Example Task", state="IN_PROGRESS", subtasks=[])
    task_list_id = service.add_task_list(name="Example Task List", tasks=[])
    service.add_task_to_list(task_id=task_id, task_list_id=task_list_id)
    task_list = service.get_task_list(task_list_id=task_list_id)
    print(task_list)
