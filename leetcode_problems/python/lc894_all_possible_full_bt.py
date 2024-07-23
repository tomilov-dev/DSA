class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def solve(self, n: int, dp: list[TreeNode]) -> list[TreeNode | None]:
        if n % 2 == 0:
            return []

        if n == 1:
            return [TreeNode()]

        if dp[n]:
            return dp[n]

        storage = []
        for i in range(1, n, 2):
            left = self.solve(i, dp)
            right = self.solve(n - i - 1, dp)

            for l in left:
                for r in right:
                    root = TreeNode()
                    root.left = l
                    root.right = r
                    storage.append(root)

        dp[n] = storage
        return storage

    def allPossibleFBT(self, n: int) -> list[TreeNode | None]:
        dp = [[] for _ in range(n + 1)]
        return self.solve(n, dp)


if __name__ == "__main__":
    n = 7
    print(Solution().allPossibleFBT(n))
