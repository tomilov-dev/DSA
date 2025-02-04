from typing import Optional
from utils import TreeNode
from utils import build_tree


class Solution:
    def smallestFromLeaf(
        self,
        root: Optional[TreeNode],
    ) -> str:
        if not root:
            return ""

        def dfs(node: Optional[TreeNode], path: str) -> None:
            nonlocal res

            if not node:
                return
            path = chr(node.val + ord("a")) + path
            if not node.left and not node.right:
                if not res or path < res:
                    res = path
                return None

            dfs(node.left, path)
            dfs(node.right, path)

        res = ""
        dfs(root, "")
        return res


if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 3, 4]
    root = build_tree(arr)
    print(Solution().smallestFromLeaf(root))
