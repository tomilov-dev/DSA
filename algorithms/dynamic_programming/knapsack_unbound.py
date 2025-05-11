class Solution:
    def knapSack(
        self,
        val: list[int],
        wt: list[int],
        capacity: int,
    ) -> int:
        n = len(val)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, capacity + 1):
                if wt[i - 1] <= j:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        val[i - 1] + dp[i][j - wt[i - 1]],
                    )
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][capacity]


class SolutionOptimized:
    def knapSack(
        self,
        val: list[int],
        wt: list[int],
        capacity: int,
    ) -> int:
        n = len(val)
        dp = [0] * (capacity + 1)
        ndp = [0] * (capacity + 1)
        for i in range(1, n + 1):
            for j in range(1, capacity + 1):
                if wt[i - 1] <= j:
                    ndp[j] = max(dp[j], val[i - 1] + ndp[j - wt[i - 1]])
                else:
                    ndp[j] = dp[j]
            dp, ndp = ndp, dp
        return dp[capacity]


class SolutionSuperOptimizied:
    def knapSack(
        self,
        val: list[int],
        wt: list[int],
        capacity: int,
    ) -> int:
        n = len(val)
        dp = [0] * (capacity + 1)
        for i in range(n):
            for j in range(wt[i], capacity + 1):
                dp[j] = max(dp[j], val[i] + dp[j - wt[i]])
        return dp[capacity]


if __name__ == "__main__":
    val = [6, 1, 7, 7]
    wt = [1, 3, 4, 5]
    capacity = 8
    print(Solution().knapSack(val, wt, capacity))
    print(SolutionOptimized().knapSack(val, wt, capacity))
    print(SolutionSuperOptimizied().knapSack(val, wt, capacity))
