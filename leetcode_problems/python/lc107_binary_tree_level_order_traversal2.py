from collections import deque
from utils import TreeNode
from utils import build_tree
from utils import print_tree


class Solution:
    def levelOrder(
        self,
        root: TreeNode | None,
    ) -> list[list[int]]:
        if root is None:
            return []

        memo = []

        q = deque([(root, 0)])
        while q:
            node, lvl = q.popleft()
            if node.left is not None:
                q.append((node.left, lvl + 1))
            if node.right is not None:
                q.append((node.right, lvl + 1))

            if len(memo) <= lvl:
                memo.append([])
            memo[lvl].append(node.val)

        return memo

    def levelOrderBottom(
        self,
        root: TreeNode | None,
    ) -> list[list[int]]:
        level_order = self.levelOrder(root)
        level_order.reverse()
        return level_order


if __name__ == "__main__":
    arr = [3, 9, 20, None, None, 15, 7]
    root = build_tree(arr)
    print_tree(root)
    print(Solution().levelOrder(root))
