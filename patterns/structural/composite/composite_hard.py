from abc import ABC
from abc import abstractmethod


class OrganizationComponent(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_salary(self) -> float:
        pass

    @abstractmethod
    def print(self) -> None:
        pass


class Employee(OrganizationComponent):
    def __init__(
        self,
        name: str,
        salary: float,
        job_title: str,
    ) -> None:
        self.name = name
        self.salary = salary
        self.job_title = job_title

    def get_name(self) -> str:
        return self.name

    def get_salary(self) -> float:
        return self.salary

    def print(self) -> None:
        print("Employee:", self.get_name())


class Manager(OrganizationComponent):
    def __init__(
        self,
        name: str,
        salary: float,
        job_title: str,
        bonus: float,
        subordinates: list[OrganizationComponent] | None = None,
    ) -> None:
        self.name = name
        self.salary = salary
        self.job_title = job_title
        self.bonus = bonus

        self.subordinates = subordinates if subordinates else []

    def get_name(self) -> str:
        return self.name

    def get_salary(self) -> float:
        total_salary = self.salary + self.bonus * len(self.subordinates)
        for subordinate in self.subordinates:
            total_salary += subordinate.get_salary()
        return total_salary

    def print(self) -> None:
        print(
            f"Manager: {self.get_name()} - {self.job_title} - Salary: {self.get_salary()}"
        )
        for subordinate in self.subordinates:
            subordinate.print()


class Department(OrganizationComponent):
    def __init__(
        self,
        name: str,
        components: list[OrganizationComponent] | None = None,
    ) -> None:
        self.name = name
        self.components = components if components else []

    def add(self, employee: OrganizationComponent) -> None:
        self.components.append(employee)

    def pop(self) -> OrganizationComponent:
        return self.components.pop()

    def get_name(self) -> str:
        return self.name

    def get_salary(self) -> float:
        return sum([c.get_salary() for c in self.components])

    def print(self) -> None:
        print("Department:", self.get_name())
        for component in self.components:
            component.print()


def client_code():
    # Пример использования
    employee1 = Employee("John Doe", 50000, "Developer")
    employee2 = Employee("Jane Smith", 60000, "Designer")
    manager1 = Manager("Alice Johnson", 80000, "Team Lead", 5000, [employee1])
    manager2 = Manager("Bob Brown", 90000, "CTO", 7000, [employee2, manager1])

    department1 = Department("HR Department")
    department1.add(employee1)
    department1.add(manager1)

    department2 = Department("IT Department")
    department2.add(employee2)
    department2.add(manager2)

    company = Department("Company")
    company.add(department1)
    company.add(department2)

    company.print()
    print(f"Total salary: {company.get_salary()}")
