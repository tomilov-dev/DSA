class TaskIterator:
    def __init__(self, tasks: list[str]) -> None:
        self.tasks = tasks
        self.__pos = 0

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.__pos < len(self.tasks):
            task = self.tasks[self.__pos]
            self.__pos += 1
            return task
        else:
            raise StopIteration


class TaskCollection:
    def __init__(self) -> None:
        self.tasks = []

    def add_task(self, task: str) -> None:
        self.tasks.append(task)

    def __iter__(self):
        return TaskIterator(self.tasks)


def client_code():
    task_collection = TaskCollection()
    task_collection.add_task("Task 1")
    task_collection.add_task("Task 2")
    task_collection.add_task("Task 3")

    for task in task_collection:
        print(task)
