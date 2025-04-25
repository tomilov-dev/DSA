"""
Решение задачи копирования документа через наивный подход
"""

from copy import copy
from copy import deepcopy


class Document:
    def __init__(
        self,
        title: str,
        content: list[str],
        metadata: dict[str, str],
    ) -> None:
        self.title = title
        self.content = content
        self.metadata = metadata

    def __str__(self):
        title = f'Title: "{self.title}"\n'
        content = "\n - ".join(self.content)
        content = f"Content: \n - {content}\n"
        meta = "\n - ".join([f"{k}: {v}" for k, v in self.metadata.items()])
        meta = f"Metadata: \n - {meta}"
        return title + content + meta


def client_code():
    doc = Document(
        title="New document",
        content=["First row", "Second row", "Third row"],
        metadata={"author": "Admin", "created_at": "2025-04-21"},
    )

    ## Каждое новое копирование заставляет нас учитывать реализацию класса
    ## И заглядывать за его кулисы (не ко всем атрибутам имеется доступ)
    doc_copy1 = Document(
        title=doc.title,
        content=copy(doc.content),
        metadata=copy(doc.metadata),
    )
    doc_copy1.content[1] = "New row 1"

    ## И переписывать один и тот же код из раза в раз
    doc_copy2 = Document(
        title=doc.title,
        content=copy(doc.content),
        metadata=copy(doc.metadata),
    )
    doc_copy2.content[1] = "New row 2"

    print(doc)
    print()
    print(doc_copy1)
    print()
    print(doc_copy2)


if __name__ == "__main__":
    client_code()
