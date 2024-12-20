from utils import TreeNode


class Solution:
    def __init__(self) -> None:
        self.f = float("inf")
        self.s = float("inf")

    def findSecondMinimumValue(
        self,
        root: TreeNode | None,
    ) -> int:
        if not root:
            return -1

        if self.f > root.val:
            self.s = self.f
            self.f = root.val
        elif self.f < root.val < self.s:
            self.s = root.val

        self.findSecondMinimumValue(root.left)
        self.findSecondMinimumValue(root.right)

        return self.s if self.s < float("inf") else -1
