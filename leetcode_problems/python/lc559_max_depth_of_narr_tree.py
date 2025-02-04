from typing import Optional
from typing import List


class Node:
    def __init__(
        self,
        val: Optional[int] = None,
        children: Optional[List["Node"]] = None,
    ):
        self.val = val
        self.children = children


class Solution:
    def dfs(
        self,
        node: Node | None,
        depth: int,
    ) -> int:
        if node is None:
            return depth

        depth += 1
        depths = [depth]
        children = node.children if node.children else []
        for child in children:
            depths.append(self.dfs(child, depth))

        return max(depths)

    def maxDepth(self, root: "Node") -> int:
        return self.dfs(root, 0)
