from utils import TreeNode
from utils import build_tree
from utils import print_tree


class Solution:
    def mergeTrees(
        self,
        n1: TreeNode | None,
        n2: TreeNode | None,
    ) -> TreeNode | None:
        if not n1 and not n2:
            return None

        root = TreeNode((n1.val if n1 else 0) + (n2.val if n2 else 0))
        root.left = self.mergeTrees(n1.left if n1 else None, n2.left if n2 else None)
        root.right = self.mergeTrees(n1.right if n1 else None, n2.right if n2 else None)

        return root


if __name__ == "__main__":
    root1 = build_tree([1, 3, 2, 5])
    root2 = build_tree([2, 1, 3, None, 4, None, 7])
    root3 = Solution().mergeTrees(root1, root2)

    print_tree(root3)
