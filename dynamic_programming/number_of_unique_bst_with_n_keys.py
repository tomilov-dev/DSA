class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


class SolutionTopDown:
    def numTrees(self, n: int) -> int:
        def backtrack(i: int) -> int:
            if i not in mem:
                mem[i] = 0
                for j in range(1, i + 1):
                    mem[i] += backtrack(j - 1) * backtrack(i - j)
            return mem[i]

        mem = {0: 1, 1: 1}
        backtrack(n)
        return mem[n]


if __name__ == "__main__":
    n = 3
    print(Solution().numTrees(n))
    print(SolutionTopDown().numTrees(n))
