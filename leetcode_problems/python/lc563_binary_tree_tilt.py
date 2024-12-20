from utils import TreeNode
from utils import build_tree
from utils import print_tree


class Solution:
    def trav(self, node: TreeNode | None) -> int:
        if not node:
            return 0

        left = self.trav(node.left)
        right = self.trav(node.right)
        self.tilt += abs(left - right)

        return left + right + node.val

    def findTilt(
        self,
        root: TreeNode | None,
    ) -> int:
        self.tilt = 0
        self.trav(root)
        return self.tilt


if __name__ == "__main__":
    arr = [4, 2, 9, 3, 5, None, 7]
    root = build_tree(arr)
    print(Solution().findTilt(root))
