from utils import TreeNode
from utils import print_tree


class Solution:
    def generateTrees(
        self,
        n: int,
    ) -> list[TreeNode | None]:
        if n == 0:
            return []

        def generate(
            start: int,
            end: int,
        ) -> list[TreeNode | None]:
            if start > end:
                return [None]

            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate(start, i - 1)
                right_trees = generate(i + 1, end)

                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)

            return all_trees

        return generate(1, n)


if __name__ == "__main__":
    n = 3
    trees = Solution().generateTrees(n)
