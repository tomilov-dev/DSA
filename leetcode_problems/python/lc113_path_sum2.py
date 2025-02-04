from typing import List
from typing import Optional
from utils import TreeNode
from utils import build_tree
from utils import print_tree


class Solution:
    def pathSum(
        self,
        root: Optional[TreeNode],
        targetSum: int,
    ) -> List[List[int]]:
        def backtrack(
            root: Optional[TreeNode],
            cursum: int = 0,
        ):
            if not root:
                return None

            cursum += root.val
            stack.append(root.val)
            if not root.left and not root.right and cursum == targetSum:
                res.append(stack[:])
            else:
                backtrack(root.left, cursum)
                backtrack(root.right, cursum)
            stack.pop()
            cursum -= root.val

        if not root:
            return []

        res = []
        stack = []
        backtrack(root, 0)
        return res


if __name__ == "__main__":
    arr = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    tree = build_tree(arr)
    targetSum = 22
    print(Solution().pathSum(tree, targetSum))
