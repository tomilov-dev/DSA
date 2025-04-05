from utils import TreeNode
from utils import print_tree


class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
        def gen(i: int, n: int) -> list[TreeNode | None]:
            if i > n:
                return [None]

            nodes = []
            for j in range(i, n + 1):
                lnodes = gen(i, j - 1)
                rnodes = gen(j + 1, n)
                for left in lnodes:
                    for right in rnodes:
                        head = TreeNode(j)
                        head.left = left
                        head.right = right
                        nodes.append(head)

            return nodes

        trees = gen(1, n)
        return [t for t in trees if t is not None]


if __name__ == "__main__":
    n = 3
    trees = Solution().generateTrees(n)
