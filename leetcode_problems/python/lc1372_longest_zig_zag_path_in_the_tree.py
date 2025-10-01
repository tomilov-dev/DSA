from utils import TreeNode


class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None, left: bool, depth: int):
            if not node:
                return
            self.ans = max(self.ans, depth)
            if node.left:
                dfs(node.left, False, depth + 1 if left else 1)
            if node.right:
                dfs(node.right, True, depth + 1 if not left else 1)

        self.ans = 0
        dfs(root, True, 0)
        dfs(root, False, 0)
        return self.ans


class SolutionTopDown:
    def longestZigZag(self, root: TreeNode | None) -> int:
        def dfs(node: TreeNode | None, left: bool) -> int:
            if not node:
                return 0
            key = (node, left)
            if key not in mem:
                if left:
                    mem[key] = 1 + dfs(node.right, False)
                else:
                    mem[key] = 1 + dfs(node.left, True)
            return mem[key]

        def traverse(node: TreeNode | None):
            if not node:
                return 0
            return max(
                dfs(node, True) - 1,
                dfs(node, False) - 1,
                traverse(node.left),
                traverse(node.right),
            )

        mem = {}
        return traverse(root)
