from utils import build_tree
from utils import print_tree
from utils import TreeNode


class Solution:
    def rec(self, node: TreeNode | None, is_left: bool):
        if node is None:
            return None

        if is_left and not node.left and not node.right:
            self.sum += node.val

        self.rec(node.left, True)
        self.rec(node.right, False)

    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        self.sum = 0
        if root is None:
            return self.sum

        self.rec(root.left, True)
        self.rec(root.right, False)
        return self.sum


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    tree = build_tree(nums)
    print_tree(tree)
