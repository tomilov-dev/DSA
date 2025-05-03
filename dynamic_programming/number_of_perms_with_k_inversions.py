class Solution:
    def countPermWithkInversions(
        self,
        n: int,
        k: int,
    ) -> int:
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for l in range(n + 1):
            dp[l][0] = 1

        for l in range(1, n + 1):
            for r in range(1, k + 1):
                for i in range(min(r, l - 1) + 1):
                    dp[l][r] = dp[l][r] + dp[l - 1][r - i]

        return dp[n][k]


if __name__ == "__main__":
    n = 3
    k = 1
    print(Solution().countPermWithkInversions(n, k))
