from typing import Union
from abc import ABC
from abc import abstractmethod


class NotEqualResult(Exception):
    pass


class TreeNode:
    def __init__(
        self,
        val,
        left: Union["TreeNode", None] = None,
        right: Union["TreeNode", None] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class BaseTraversal(ABC):
    @abstractmethod
    def recursive(self, root: TreeNode | None) -> list[int]:
        pass

    @abstractmethod
    def iterative(self, root: TreeNode | None) -> list[int]:
        pass

    def is_equal(self, root: TreeNode | None) -> bool:
        m1 = self.recursive(root)
        m2 = self.iterative(root)
        if len(m1) != len(m2):
            raise NotEqualResult("Конечные массивы не совпадают по размеру")

        errors: list[str] = []
        for i, v in enumerate(m1):
            if v != m2[i]:
                err = f"Ошибка на индексе {i}: {v} != {m2[i]}"
                errors.append(err)
        if len(errors) != 0:
            raise NotEqualResult("\n".join(errors))
        return True


class PreorderTraversal(BaseTraversal):
    def _recursive(self, node: TreeNode | None, stack: list[int]) -> list[int]:
        if node is None:
            return stack

        print(node.val)
        stack.append(node.val)
        self._recursive(node.left, stack)
        self._recursive(node.right, stack)
        return stack

    def recursive(self, root: TreeNode | None) -> list[int]:
        stack = []
        return self._recursive(root, stack)

    def iterative(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        result = []
        call_stack = [root]
        while call_stack:
            node = call_stack.pop()

            print(node.val)
            result.append(node.val)
            if node.right:
                call_stack.append(node.right)
            if node.left:
                call_stack.append(node.left)
        return result


class PostorderTraversal(BaseTraversal):
    def _recursive(self, node: TreeNode | None, stack: list[int]) -> list[int]:
        if node is None:
            return stack

        self._recursive(node.left, stack)
        self._recursive(node.right, stack)
        print(node.val)
        stack.append(node.val)
        return stack

    def recursive(self, root: TreeNode | None) -> list[int]:
        stack = []
        return self._recursive(root, stack)

    def iterative(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        result = []
        call_stack = [root]
        while call_stack:
            node = call_stack.pop()
            result.append(node.val)
            if node.left:
                call_stack.append(node.left)
            if node.right:
                call_stack.append(node.right)
        return list(reversed(result))


class InorderTraversal(BaseTraversal):
    def _recursive(self, node: TreeNode | None, stack: list[int]) -> list[int]:
        if node is None:
            return stack

        self._recursive(node.left, stack)
        print(node.val)
        stack.append(node.val)
        self._recursive(node.right, stack)
        return stack

    def recursive(self, root: TreeNode | None) -> list[int]:
        stack = []
        return self._recursive(root, stack)

    def iterative(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        result = []
        stack: list[TreeNode] = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            print(node.val)
            result.append(node.val)
            node = node.right
        return result


def get_root() -> TreeNode:
    root = TreeNode(1)

    l1 = TreeNode(2)
    r1 = TreeNode(3)

    l2 = TreeNode(4)
    r2 = TreeNode(5)

    l1.left = l2
    l2.right = r2

    root.left = l1
    root.right = r1

    return root


if __name__ == "__main__":
    root = get_root()

    preorder = PreorderTraversal()
    # preorder.recursive(root)
    # preorder.iterative(root)
    # preorder.is_equal(root)

    postorder = PostorderTraversal()
    # postorder.recursive(root)
    # postorder.iterative(root)
    # postorder.is_equal(root)

    inorder = InorderTraversal()
    # inorder.recursive(root)
    # inorder.iterative(root)
    inorder.is_equal(root)
