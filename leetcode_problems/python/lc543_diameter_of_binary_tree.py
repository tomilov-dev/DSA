from utils import TreeNode
from utils import build_tree


class Solution:
    def trav(
        self,
        node: TreeNode | None,
    ) -> int:
        if not node:
            return 0

        left = self.trav(node.left)
        right = self.trav(node.right)
        self.max_diam = max(self.max_diam, left + right)

        return max(left, right) + 1

    def diameterOfBinaryTree(
        self,
        root: TreeNode | None,
    ) -> int:
        self.max_diam = 0
        self.trav(root)
        return self.max_diam


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    root = build_tree(arr)
    print(Solution().diameterOfBinaryTree(root))
