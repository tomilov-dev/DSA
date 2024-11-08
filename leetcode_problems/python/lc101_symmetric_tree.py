class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def check(
        self,
        l: TreeNode | None,
        r: TreeNode | None,
    ) -> bool:
        if l is None or r is None:
            return l is None and r is None
        if l.val != r.val:
            return False
        return self.check(l.left, r.right) and self.check(l.right, r.left)

    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return False
        return self.check(root.left, root.right)


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(Solution().isSymmetric(root))
