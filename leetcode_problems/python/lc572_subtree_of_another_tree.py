from utils import TreeNode
from utils import build_tree


class Solution:
    def same(
        self,
        s: TreeNode | None,
        t: TreeNode | None,
    ) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return self.same(s.left, t.left) and self.same(s.right, t.right)

    def trav(
        self,
        node: TreeNode | None,
        sub: TreeNode | None,
    ) -> None:
        if not node or not sub:
            return None

        if self.same(node, sub):
            self.res = True
            return None

        self.trav(node.left, sub)
        self.trav(node.right, sub)

    def isSubtree(
        self,
        root: TreeNode | None,
        subRoot: TreeNode | None,
    ) -> bool:
        self.res = False
        self.trav(root, subRoot)
        return self.res


if __name__ == "__main__":
    arr1 = [3, 4, 5, 1, 2]
    arr2 = [4, 1, 2]

    root = build_tree(arr1)
    subroot = build_tree(arr2)
    print(Solution().isSubtree(root, subroot))
