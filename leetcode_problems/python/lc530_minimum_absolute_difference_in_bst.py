from utils import TreeNode
from utils import build_tree
from utils import print_tree


class Solution:
    def __init__(self) -> None:
        self.min_diff = 10**7
        self.prev = 10**7

    def trav(
        self,
        node: TreeNode | None,
    ) -> None:
        if not node:
            return None

        self.trav(node.left)

        cur_diff = abs(self.prev - node.val)
        self.min_diff = min(self.min_diff, cur_diff)
        self.prev = node.val

        self.trav(node.right)

    def getMinimumDifference(
        self,
        root: TreeNode | None,
    ) -> int:
        self.trav(root)
        return self.min_diff


if __name__ == "__main__":
    arr = [4, 2, 6, 1, 3]
    arr = [236, 104, 701, None, 227, None, 911]
    root = build_tree(arr)
    print_tree(root)

    print(Solution().getMinimumDifference(root))
