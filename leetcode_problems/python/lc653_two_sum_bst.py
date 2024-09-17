class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def trav(self, node: TreeNode | None, hook):
        if node is None:
            return

        if hook is not None:
            hook(node.val)

        self.trav(node.left, hook)
        self.trav(node.right, hook)

    def findTarget(self, root: TreeNode | None, k: int) -> bool:
        mapper = dict()

        def update_mapper(val):
            mapper[val] = mapper.get(val, 0) + 1

        self.trav(root, update_mapper)

        for num, freq in mapper.items():
            if freq >= 2 and num + num == k:
                return True
            elif k - num != num and mapper.get(k - num, 0) > 0:
                return True

        return False


if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(7)

    print(Solution().findTarget(root, 9))
