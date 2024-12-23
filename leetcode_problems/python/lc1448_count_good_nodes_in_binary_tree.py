from utils import TreeNode
from utils import build_tree
from utils import print_tree


class Solution:
    def trav(
        self,
        node: TreeNode | None,
        maxi: int = 0,
    ) -> None:
        if not node:
            return None

        if node.val >= maxi:
            self.c += 1
            maxi = node.val

        self.trav(node.left, maxi)
        self.trav(node.right, maxi)

    def goodNodes(
        self,
        root: TreeNode | None,
    ) -> int:
        if not root:
            return 0

        self.c = 0
        self.trav(root, 0)
        return self.c


if __name__ == "__main__":
    arr = [3, 1, 4, 3, None, 1, 5]
    root = build_tree(arr)
    print(Solution().goodNodes(root))
