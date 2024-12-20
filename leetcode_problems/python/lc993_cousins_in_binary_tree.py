from collections import deque
from utils import TreeNode
from utils import build_tree


class Solution:
    def isCousins(
        self,
        root: TreeNode | None,
        x: int,
        y: int,
    ) -> bool:
        if not root:
            return False

        q = deque([(root, 0)])
        flat = [[(root, root)]]
        while q:
            n, i = q.popleft()
            if n:
                if len(flat) <= i + 1:
                    flat.append([])
                if n.left:
                    flat[i + 1].append((n.left, n))
                    q.append((n.left, i + 1))
                if n.right:
                    flat[i + 1].append((n.right, n))
                    q.append((n.right, i + 1))

        for lvl in flat:
            mlvl = {}
            for n, p in lvl:
                if n.val != x and n.val != y:
                    continue

                if p.val not in mlvl:
                    mlvl[p.val] = []
                mlvl[p.val].append(n.val)

            if len(mlvl) >= 2:
                return True
        return False


class Solution2:
    def isCousins(
        self,
        root: TreeNode | None,
        x: int,
        y: int,
    ) -> bool:
        if not root:
            return False

        q = deque([(root, root)])
        while q:
            level_size = len(q)
            x_parent = y_parent = None

            for _ in range(level_size):
                node, parent = q.popleft()

                if node.val == x:
                    x_parent = parent
                if node.val == y:
                    y_parent = parent

                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))

            if x_parent and y_parent:
                return x_parent != y_parent
            if x_parent or y_parent:
                return False

        return False


if __name__ == "__main__":
    root = build_tree([1, 2, 3, None, 4, None, 5])
    x = 5
    y = 4
    print(Solution().isCousins(root, x, y))
