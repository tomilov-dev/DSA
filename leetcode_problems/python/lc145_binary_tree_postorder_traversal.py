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

        self.preorder(node.left, mem)
        self.preorder(node.right, mem)
        mem.append(node.val)

    def postorderTraversal(
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

    data = Solution().postorderTraversal(root)
    print(data)
