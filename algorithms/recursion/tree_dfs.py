from typing import Union


class TreeNode:
    def __init__(
        self,
        value: int,
        left: Union["TreeNode", None] = None,
        right: Union["TreeNode", None] = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right


class PreorderDFS:
    def traverse(self, node: TreeNode | None) -> None:
        if not node:
            return None

        print(node.value)
        self.traverse(node.left)
        self.traverse(node.right)


class InorderDFS:
    def traverse(self, node: TreeNode | None) -> None:
        if not node:
            return None

        self.traverse(node.left)
        print(node.value)
        self.traverse(node.right)


class PostorderDFS:
    def traverse(self, node: TreeNode | None) -> None:
        if not node:
            return None

        self.traverse(node.left)
        self.traverse(node.right)
        print(node.value)


if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)

    PreorderDFS().traverse(root)
    PostorderDFS().traverse(root)
    InorderDFS().traverse(root)
