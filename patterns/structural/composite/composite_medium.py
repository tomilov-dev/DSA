from abc import ABC
from abc import abstractmethod


class MenuComponent(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_price(self) -> float:
        pass

    @abstractmethod
    def print(self) -> None:
        pass


class Dish(MenuComponent):
    def __init__(
        self,
        name: str,
        price: float,
    ) -> None:
        self.name = name
        self.price = price

    def get_name(self) -> str:
        return f"Dish: {self.name}"

    def get_price(self) -> float:
        return self.price

    def print(self) -> None:
        name = self.get_name()
        print(f"{name} - {self.get_price()}")


class Drink(MenuComponent):
    def __init__(
        self,
        name: str,
        price: float,
        alcohol: bool,
    ) -> None:
        self.name = name
        self.price = price
        self.alcohol = alcohol

    def get_name(self) -> str:
        return f"Drink: {self.name}"

    def get_price(self) -> float:
        return self.price

    def print(self) -> None:
        name = self.get_name()
        alco = "With" if self.alcohol else "Without"
        print(f"{name} - {self.get_price()} - {alco} alcohol")


class Category(MenuComponent):
    def __init__(self, name: str) -> None:
        self.name = name
        self.menu: list[MenuComponent] = []

    def add(self, component: MenuComponent) -> None:
        self.menu.append(component)

    def pop(self) -> MenuComponent:
        return self.menu.pop()

    def get_name(self) -> str:
        return f"Category: {self.name}"

    def get_price(self) -> float:
        return sum([c.get_price() for c in self.menu])

    def print(self) -> None:
        print(self.get_name())
        for component in self.menu:
            component.print()


def client_code():
    dish1 = Dish("Caesar Salad", 5.99)
    dish2 = Dish("Spaghetti Carbonara", 8.99)
    drink1 = Drink("Coca Cola", 1.99, False)
    drink2 = Drink("Espresso", 2.49, False)

    appetizers = Category("Appetizers")
    appetizers.add(dish1)

    main_courses = Category("Main Courses")
    main_courses.add(dish2)

    drinks = Category("Drinks")
    drinks.add(drink1)
    drinks.add(drink2)

    menu = Category("Menu")
    menu.add(appetizers)
    menu.add(main_courses)
    menu.add(drinks)

    menu.print()
    print(f"Total price: {menu.get_price()}")
