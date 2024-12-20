from collections import deque
from utils import TreeNode
from utils import build_tree
from utils import print_tree


class Solution:
    def averageOfLevels(
        self,
        root: TreeNode | None,
    ) -> list[float]:
        if not root:
            return []

        queue = deque([root])
        result = []
        while queue:
            sum = 0
            qty = 0
            add = []
            while queue:
                n = queue.popleft()
                if not n:
                    continue

                l = n.left
                r = n.right
                sum += n.val
                qty += 1

                add.append(l)
                add.append(r)

            if qty > 0:
                result.append(sum / qty)

            while add:
                n = add.pop()
                queue.appendleft(n)

        return result


class Solution2:
    def averageOfLevels(
        self,
        root: TreeNode | None,
    ) -> list[float]:
        if not root:
            return []

        queue = deque([root])
        result = []
        while queue:
            level_sum = 0
            level_count = len(queue)
            for _ in range(level_count):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_sum / level_count)

        return result


if __name__ == "__main__":
    root = build_tree([3, 9, 20, None, None, 15, 7])
    print(Solution().averageOfLevels(root))
