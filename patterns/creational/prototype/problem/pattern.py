"""
Решение задачи копирования документа через паттерн Prototype
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

    def clone(self) -> "Document":
        return Document(
            title=self.title,
            content=copy(self.content),
            metadata=copy(self.metadata),
        )

    def __copy__(self):
        # Дополнительный метод копирования, который работает с copy.copy()
        return Document(
            title=self.title,
            content=copy(self.content),
            metadata=copy(self.metadata),
        )

    def __deepcopy__(self, memo):
        # Дополнительный метод копирования, который работает с copy.deepcopy()
        return Document(
            title=deepcopy(self.title, memo),
            content=deepcopy(self.content, memo),
            metadata=deepcopy(self.metadata, memo),
        )

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

    ## Копирование максимально упрощено
    doc_copy1 = doc.clone()
    doc_copy1.content[1] = "New row 1"

    ## Вызываем метод и получаем полную копию объекта
    doc_copy2 = doc_copy1.clone()
    doc_copy2.content[1] = "New row 2"

    print(doc)
    print()
    print(doc_copy1)
    print()
    print(doc_copy2)


if __name__ == "__main__":
    client_code()
