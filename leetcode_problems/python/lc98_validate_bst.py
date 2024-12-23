from utils import TreeNode
from utils import build_tree
from utils import print_tree


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def validate(node: TreeNode | None, low: float, high: float) -> bool:
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(
                node.right,
                node.val,
                high,
            )

        return validate(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    arr = [5, 1, 4, None, None, 3, 6]
    arr = [2, 1, 3]
    arr = [1, None, 1]
    arr = [5, 4, 6, None, None, 3, 7]
    root = build_tree(arr)
    print_tree(root)
    print(Solution().isValidBST(root))
