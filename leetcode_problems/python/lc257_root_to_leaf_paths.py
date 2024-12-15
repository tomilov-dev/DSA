from utils import TreeNode
from utils import build_tree
from utils import print_tree


class Solution:
    def rec(self, node: TreeNode | None, stack: list[int]) -> None:
        if node is None:
            return
        stack.append(node.val)
        if node.left is None and node.right is None:
            self.paths.append("->".join(map(str, stack)))
        else:
            self.rec(node.left, stack)
            self.rec(node.right, stack)
        stack.pop()

    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        if root is None:
            return []

        self.paths = []
        self.rec(root, [])
        return self.paths


if __name__ == "__main__":
    root = build_tree([1, 2, 3, None, 5])
    print(Solution().binaryTreePaths(root))
