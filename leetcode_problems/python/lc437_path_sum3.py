from utils import TreeNode
from utils import build_tree
from utils import print_tree


class Solution:
    def dfs(
        self,
        node: TreeNode | None,
        curr_sum: int,
        target_sum: int,
    ) -> int:
        if node is None:
            return 0

        curr_sum += node.val
        paths = int(curr_sum == target_sum)

        paths += self.dfs(node.left, curr_sum, target_sum)
        paths += self.dfs(node.right, curr_sum, target_sum)

        return paths

    def pathSum(
        self,
        root: TreeNode | None,
        targetSum: int,
    ) -> int:
        if root is None:
            return 0

        return (
            self.dfs(root, 0, targetSum)
            + self.pathSum(root.left, targetSum)
            + self.pathSum(root.right, targetSum)
        )


if __name__ == "__main__":
    arr = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    targetSum = 8
    root = build_tree(arr)

    print_tree(root)
    print(Solution().pathSum(root, targetSum))
