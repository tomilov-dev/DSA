from abc import ABC
from abc import abstractmethod


class IUIElement(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class Button(IUIElement):
    pass


class Checkbox(IUIElement):
    pass


class TextField(IUIElement):
    pass


class WindowsButton(Button):
    def render(self) -> str:
        return "Windows button\n"


class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "Windows checkbox\n"


class WindowsTextField(TextField):
    def render(self) -> str:
        return "Windows text field\n"


class MacOSButton(Button):
    def render(self) -> str:
        return "MacOS button\n"


class MacOSCheckbox(Checkbox):
    def render(self) -> str:
        return "MacOS checkbox\n"


class MacOSTextField(TextField):
    def render(self) -> str:
        return "MacOS text field\n"


class LinuxButton(Button):
    def render(self) -> str:
        return "Linux button\n"


class LinuxCheckbox(Checkbox):
    def render(self) -> str:
        return "Linux checkbox\n"


class LinuxTextField(TextField):
    def render(self) -> str:
        return "Linux text field\n"


class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

    @abstractmethod
    def create_text_field(self) -> TextField:
        pass


class WindowsUIFactory(UIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

    def create_text_field(self) -> TextField:
        return WindowsTextField()


class MacOSUIFactory(UIFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()

    def create_text_field(self) -> TextField:
        return MacOSTextField()


class LinuxUIFactory(UIFactory):
    def create_button(self) -> Button:
        return LinuxButton()

    def create_checkbox(self) -> Checkbox:
        return LinuxCheckbox()

    def create_text_field(self) -> TextField:
        return LinuxTextField()


def client_code(ui_factory: UIFactory):
    button = ui_factory.create_button()
    checkbox = ui_factory.create_checkbox()
    text_field = ui_factory.create_text_field()

    page = f"{button.render()}{checkbox.render()}{text_field.render()}"
