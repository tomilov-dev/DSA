from typing import Union


class Node:
    def __init__(
        self,
        data: int,
        next: Union["Node", None] = None,
    ) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return str(self.data)


class Solution:
    def delete(self, node: Node | None) -> None:
        if node:
            self.delete(node.next)
            node.next = None


if __name__ == "__main__":
    root = Node(0)
    root.next = Node(1)
    root.next.next = Node(2)
    root.next.next.next = Node(3)

    Solution().delete(root)
