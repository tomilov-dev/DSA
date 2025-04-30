class Solution:
    def findCatalan(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]


class SolutionTopDown:
    def findCatalan(self, n: int) -> int:
        def backtrack(i: int) -> int:
            if i not in mem:
                mem[i] = 0
                for j in range(0, i):
                    mem[i] += backtrack(j) * backtrack(i - j - 1)
            return mem[i]

        mem = {0: 1, 1: 1}
        backtrack(n)
        return mem[n]


if __name__ == "__main__":
    n = 6
    print(Solution().findCatalan(n))
    print(SolutionTopDown().findCatalan(n))
