"""
Решения задачи обхода директории файловой системы (наивный подход)
"""

from abc import ABC
from typing import Union


class IFileSystemComponent(ABC):
    def __init__(
        self,
        name: str,
        childrens: Union[list["IFileSystemComponent"], None] = None,
    ) -> None:
        self.name = name
        if not childrens:
            childrens = []
        self.childrens = childrens


class File(IFileSystemComponent):
    pass


class Directory(IFileSystemComponent):
    pass


class FileCollection:
    def __init__(self, root_dir: IFileSystemComponent) -> None:
        self.root_dir = root_dir

    def find(
        self,
        name: str,
        root: IFileSystemComponent | None,
    ) -> IFileSystemComponent | None:
        if not root:
            root = self.root_dir

        if root.name == name:
            return root
        for children in root.childrens:
            found = self.find(name, children)
            if found:
                return found

        return None

    def get_files(self, dir_name: str) -> IFileSystemComponent:
        path = dir_name.split("/")
        prev = self.root_dir
        for name in path:
            cur = self.find(name, prev)
            if not cur:
                raise ValueError("Path does not exists")
            prev = cur
        return cur


def client_code():
    root = Directory(
        "root",
        [
            File("file1.txt"),
            Directory(
                "docs",
                [
                    File("doc1.txt"),
                    File("doc2.txt"),
                ],
            ),
            Directory(
                "images",
                [
                    File("img1.png"),
                    File("img2.jpg"),
                ],
            ),
        ],
    )

    collection = FileCollection(root)
    docs = collection.get_files("root/docs")
    for file in docs.childrens:
        print(file.name)


if __name__ == "__main__":
    client_code()
