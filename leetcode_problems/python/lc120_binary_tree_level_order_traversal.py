from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(
        self,
        root: TreeNode | None,
    ) -> list[list[int]]:
        levels: list[list[int]] = []

        q = deque([(root, 0)])
        while q:
            node, level = q.popleft()
            if node is None:
                continue

            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)

            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return levels


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(Solution().levelOrder(root))
