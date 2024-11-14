from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def min_depth(self, node: TreeNode | None) -> int:
        if node is None:
            return 10**6

        if node.left is None and node.right is None:
            return 1

        left_depth = self.min_depth(node.left)
        right_depth = self.min_depth(node.right)

        return min(left_depth, right_depth) + 1

    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        return self.min_depth(root)


class SolutionQueue:
    def minDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0

        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if node.left is None and node.right is None:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return 0


if __name__ == "__main__":
    head = TreeNode(3)
    head.left = TreeNode(9)
    head.right = TreeNode(20)
    head.right.left = TreeNode(15)
    head.right.right = TreeNode(7)

    print(Solution().minDepth(head))  # Output: 2

    head = TreeNode(2)
    head.right = TreeNode(3)
    head.right.right = TreeNode(4)
    head.right.right.right = TreeNode(5)
    head.right.right.right.right = TreeNode(6)

    print(Solution().minDepth(head))  # Output: 5
