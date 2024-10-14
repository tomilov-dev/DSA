#### --- MODEL START --- ####


class NotFoundError(Exception):
    pass


class IdNotSetted(Exception):
    pass


class Contact:
    def __init__(
        self,
        name: str,
        phone: str,
        email: str,
    ) -> None:
        self.name = name
        self.phone = phone
        self.email = email

        self.__id = None

    @property
    def id(self) -> int:
        if self.__id is None:
            raise IdNotSetted
        return self.__id

    @id.setter
    def set_id(self, id: int) -> None:
        self.__id = id


class ContactManager:
    def __init__(self) -> None:
        self._contacts: dict[int, Contact] = {}
        self._index = 0

    def add_contact(self, contact: Contact) -> Contact:
        id = self._index
        self._index += 1
        contact.set_id = id
        self._contacts[id] = contact
        return contact

    def delete_contact(self, id: int) -> Contact:
        if id not in self._contacts:
            raise NotFoundError
        contact = self._contacts[id]
        del self._contacts[id]
        return contact

    def get_contact_by_id(self, id: int) -> Contact:
        contact = self._contacts.get(id, None)
        if contact is None:
            raise NotFoundError
        return contact

    def get_contacts_by_name(self, name: str) -> list[Contact]:
        contacts = []
        for contact in self._contacts.values():
            if contact.name == name:
                contacts.append(contact)
        return contacts


#### --- MODEL END --- ####


#### --- VIEW START --- ####


class ContactView:
    def contact_view(self, contact: Contact) -> str:
        return f"ID: {contact.id}, Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}"

    def show_message(self, message: str) -> None:
        print(message)

    def show_contact(self, contact: Contact) -> None:
        print(self.contact_view(contact))

    def show_contacts(self, contacts: list[Contact]) -> None:
        for contact in contacts:
            print(self.contact_view(contact))

    def show_error(self, error: Exception) -> None:
        print(error)


#### --- VIEW END --- ####


#### --- CONTROLLER START --- ####


class ContactController:
    def __init__(
        self,
        contact_manager: ContactManager,
        contact_view: ContactView,
    ) -> None:
        self._contact_manager = contact_manager
        self._contact_view = contact_view

    def add_contact(self) -> None:
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        contact = self._contact_manager.add_contact(Contact(name, phone, email))
        self._contact_view.show_message("Contact added:")
        self._contact_view.show_contact(contact)

    def delete_contact(self):
        id = int(input("Enter ID: "))
        try:
            contact = self._contact_manager.delete_contact(id)
            self._contact_view.show_message("Contact deleted:")
            self._contact_view.show_contact(contact)
        except NotFoundError:
            self._contact_view.show_message(f"Not found contact with id: {id}")

    def get_contact_by_id(self):
        id = int(input("Enter ID: "))
        try:
            contact = self._contact_manager.get_contact_by_id(id)
            self._contact_view.show_message("Contact:")
            self._contact_view.show_contact(contact)
        except NotFoundError:
            self._contact_view.show_message(f"Not found contact with id: {id}")

    def get_contacts_by_name(self):
        name = input("Enter name: ")
        contacts = self._contact_manager.get_contacts_by_name(name)
        self._contact_view.show_message("Contacts:")
        self._contact_view.show_contacts(contacts)

    def help(self) -> None:
        self._contact_view.show_message(
            "Commands:\n"
            "add - add contact\n"
            "delete - delete contact\n"
            "get_by_id - get contact by id\n"
            "get_by_name - get contacts by name\n"
            "help - show help"
        )

    def handle(self, command: str) -> None:
        if command == "add":
            self.add_contact()
        elif command == "delete":
            self.delete_contact()
        elif command == "get_by_id":
            self.get_contact_by_id()
        elif command == "get_by_name":
            self.get_contacts_by_name()
        elif command == "help":
            self.help()
        else:
            self._contact_view.show_message("Unknown command")


#### --- CONTROLLER END --- ####


def main():
    view = ContactView()
    manager = ContactManager()
    controller = ContactController(manager, view)
    while True:
        command = input("Enter command (help): ")
        if command == "exit":
            break

        controller.handle(command)
        print("\n")


if __name__ == "__main__":
    main()
