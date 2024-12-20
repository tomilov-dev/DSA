from utils import TreeNode
from utils import build_tree


class Solution:
    def trav(
        self,
        node: TreeNode | None,
    ) -> None:
        if not node:
            return None

        self.mem[node.val] = self.mem.get(node.val, 0) + 1
        self.trav(node.left)
        self.trav(node.right)

    def findMode(
        self,
        root: TreeNode | None,
    ) -> list[int]:
        if not root:
            return []

        self.mem = {}
        self.trav(root)

        maxfq = 0
        for k, v in self.mem.items():
            maxfq = max(maxfq, v)

        result = []
        for k, v in self.mem.items():
            if v == maxfq:
                result.append(k)

        return result


class Solution2:
    def __init__(self) -> None:
        self.prev: TreeNode | None = None
        self.curr_count = 0
        self.max_count = 0
        self.modes = []

    def trav(
        self,
        node: TreeNode | None,
    ) -> None:
        if not node:
            return None

        self.trav(node.left)

        if self.prev is None or self.prev.val != node.val:
            self.curr_count = 1
        elif self.prev.val == node.val:
            self.curr_count += 1

        if self.curr_count > self.max_count:
            self.max_count = self.curr_count
            self.modes = [node.val]
        elif self.curr_count == self.max_count:
            self.modes.append(node.val)

        self.prev = node

        self.trav(node.right)

    def findMode(
        self,
        root: TreeNode | None,
    ) -> list[int]:
        if not root:
            return []

        self.trav(root)
        return self.modes


if __name__ == "__main__":
    arr = [1, None, 2, 2]
    root = build_tree(arr)
    print(Solution2().findMode(root))
