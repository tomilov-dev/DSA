class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def move(
        self,
        node: TreeNode | None,
        currentSum: int,
        targetSum: int,
    ) -> bool:
        if node is None:
            return False
        currentSum += node.val
        if targetSum == currentSum and not node.left and not node.right:
            return True

        return self.move(
            node.left,
            currentSum,
            targetSum,
        ) or self.move(
            node.right,
            currentSum,
            targetSum,
        )

    def hasPathSum(
        self,
        root: TreeNode | None,
        targetSum: int,
    ) -> bool:
        if root is None:
            return False

        return self.move(
            root,
            currentSum=0,
            targetSum=targetSum,
        )


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    targetSum = 22

    print(Solution().hasPathSum(root, targetSum))
