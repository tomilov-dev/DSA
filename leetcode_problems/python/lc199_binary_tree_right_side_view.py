from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(
        self,
        node: TreeNode | None,
    ) -> list[list[int]]:
        levels: list[list[int]] = []
        q = deque([(node, 0)])
        while q:
            node, l = q.popleft()  # l for level
            if node is None:
                continue

            # hookahe place
            if len(levels) == l:
                levels.append([])
            levels[l].append(node.val)

            if node.left:
                q.append((node.left, l + 1))
            if node.right:
                q.append((node.right, l + 1))

        return levels

    def rightSideView(
        self,
        root: TreeNode | None,
    ) -> list[int]:
        inordered = self.inorder(root)
        return [m[-1] for m in inordered]


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)

    print(Solution().rightSideView(root))
