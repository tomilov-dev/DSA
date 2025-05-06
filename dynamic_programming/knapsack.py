class Solution:
    def knapsack(
        self,
        w: int,
        val: list[int],
        wt: list[int],
    ) -> int:
        n = len(val)
        dp = [[0] * (w + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, w + 1):
                if wt[i - 1] <= j:
                    # pick item
                    dp[i][j] = max(
                        dp[i - 1][j],
                        val[i - 1] + dp[i - 1][j - wt[i - 1]],
                    )
                else:
                    # not pick item
                    dp[i][j] = dp[i - 1][j]

        return dp[n][w]


class SolutionOptimized:
    def knapsack(
        self,
        w: int,
        val: list[int],
        wt: list[int],
    ) -> int:
        n = len(val)
        dp = [0] * (w + 1)
        ndp = [0] * (w + 1)
        for i in range(1, n + 1):
            for j in range(1, w + 1):
                if wt[i - 1] <= j:
                    # pick item
                    ndp[j] = max(
                        dp[j],
                        val[i - 1] + dp[j - wt[i - 1]],
                    )
                else:
                    # not pick item
                    ndp[j] = dp[j]
            dp, ndp = ndp, dp
        return dp[w]


class SolutionSuperOptimized:
    def knapsack(
        self,
        w: int,
        val: list[int],
        wt: list[int],
    ) -> int:
        n = len(val)
        dp = [0] * (w + 1)
        for i in range(n):
            for j in range(w, wt[i] - 1, -1):
                dp[j] = max(dp[j], val[i] + dp[j - wt[i]])
        return dp[n]


if __name__ == "__main__":
    w = 4
    val = [1, 2, 3]
    wt = [4, 5, 1]
    print(Solution().knapsack(w, val, wt))
    print(SolutionOptimized().knapsack(w, val, wt))
    print(SolutionSuperOptimized().knapsack(w, val, wt))
