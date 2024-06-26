from typing import Callable


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def inorder_traversal(
        self,
        node: TreeNode,
        hook: Callable[[TreeNode], None],
    ) -> list[TreeNode]:
        if node is None:
            return

        self.inorder_traversal(node.left, hook)
        hook(node)
        self.inorder_traversal(node.right, hook)

    def balanced_bst(
        self,
        nodes: list[TreeNode],
        start: int,
        end: int,
    ) -> TreeNode:
        if start > end:
            return None

        mid = start + (end - start) // 2

        node = nodes[mid]
        node.left = self.balanced_bst(nodes, start, mid - 1)
        node.right = self.balanced_bst(nodes, mid + 1, end)

        return node

    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_nodes: list[TreeNode] = []
        self.inorder_traversal(root, sorted_nodes.append)
        return self.balanced_bst(sorted_nodes, 0, len(sorted_nodes) - 1)


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)

    sol = Solution()
    root = sol.balanceBST(root)

    print(root)
