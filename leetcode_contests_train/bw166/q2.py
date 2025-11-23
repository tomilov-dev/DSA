class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        dp = [10**10] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(max(0, i - 3), i):
                dp[i] = min(
                    dp[i],
                    dp[j] + costs[i - 1] + (j - i) ** 2,
                )
        return dp[n]


if __name__ == "__main__":
    n = 4
    costs = [1, 2, 3, 4]
    n = 4
    costs = [5, 1, 6, 2]
    print(Solution().climbStairs(n, costs))
