from utils import TreeNode
from utils import build_tree
from utils import print_tree


class Solution:
    """
    Рекурсивное решение с прямым порядком обхода.
    Идея в том, чтобы менять указатели и возвращать последний элемент в новом списке.
    Вместе с этим мы обязаны занулять левые указатели в конце операций.
    """

    def trav(
        self,
        node: TreeNode | None,
    ) -> TreeNode | None:
        if not node:
            return None

        left = self.trav(node.left)
        right = self.trav(node.right)

        if not left and not right:
            return node
        elif not right:
            node.right = node.left
            node.left = None
            return left
        elif not left:
            node.left = None
            return right
        else:
            temp = node.right
            node.right = node.left
            left.right = temp
            node.left = None
            return right

    def flatten(
        self,
        root: TreeNode | None,
    ) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        self.trav(root)


class Solution2:
    """
    Рекурсивное решение с обратным порядком обхода.
    Заместо обхода левых поддеревьев мы сначала обходим правые.
    Таким образом наша цель - достичь конца будущего списка.
    Мы собираем список с конца и храним переменную, которая указывает на верхний элемент нового списка.
    """

    def traverse(self, node: TreeNode | None):
        if not node:
            return None

        self.traverse(node.right)
        self.traverse(node.left)

        node.right = self.prev
        node.left = None
        self.prev = node

    def flatten(
        self,
        root: TreeNode | None,
    ) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.prev = None
        self.traverse(root)


if __name__ == "__main__":
    arr = [1, 2, 5, 3, 4, None, 6]
    root = build_tree(arr)
    Solution2().flatten(root)

    print_tree(root)
