from utils import TreeNode


class Solution:
    def btd(self, binary_list):
        decimal_number = 0
        for digit in binary_list:
            decimal_number = decimal_number * 2 + digit
        return decimal_number

    def trav(self, node: TreeNode | None, stack: list[int]) -> None:
        if node is None:
            return None

        stack.append(node.val)
        if not node.left and not node.right:
            self.res.append(self.btd(stack))

        self.trav(node.left, stack)
        self.trav(node.right, stack)
        stack.pop()

    def sumRootToLeaf(self, root: TreeNode | None) -> int:
        self.res = []
        self.trav(root, [])
        return sum(self.res)
