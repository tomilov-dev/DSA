from utils import TreeNode


class Solution:
    def __init__(self) -> None:
        self.s = 0

    def rangeSumBST(
        self,
        root: TreeNode | None,
        low: int,
        high: int,
    ) -> int:
        if not root:
            return self.s

        if low <= root.val <= high:
            print("+", root.val)
            self.s += root.val

        self.rangeSumBST(root.left, low, high)
        self.rangeSumBST(root.right, low, high)

        return self.s
