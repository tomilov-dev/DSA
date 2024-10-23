class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorder(
        self,
        node: TreeNode | None,
        mem: list[int],
    ):
        if node is None:
            return

        mem.append(node.val)
        self.preorder(node.left, mem)
        self.preorder(node.right, mem)

    def preorderTraversal(
        self,
        root: TreeNode | None,
    ) -> list[int]:
        mem = []
        self.preorder(root, mem)
        return mem


if __name__ == "__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    data = Solution().preorderTraversal(root)
    print(data)
