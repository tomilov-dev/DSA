class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(1, n):
            if 2 <= i * 2 <= n:
                dp[i * 2] = dp[i]
            if 2 <= i * 2 + 1 <= n:
                dp[i * 2 + 1] = dp[i] + dp[i + 1]
        return max(dp)


if __name__ == "__main__":
    n = 7
    print(Solution().getMaximumGenerated(n))
