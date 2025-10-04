class Solution:
    def knapsack(
        self,
        capacity: int,
        values: list[int],
        weights: list[int],
    ) -> int:
        m = len(values)
        dp = [[0] * (capacity + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            w = weights[i - 1]
            v = values[i - 1]
            for j in range(1, capacity + 1):
                if w <= j:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        v + dp[i][j - w],
                    )
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m][capacity]


class SolutionOptimal:
    def knapsack(
        self,
        capacity: int,
        values: list[int],
        weights: list[int],
    ) -> int:
        m = len(values)
        dp = [0] * (capacity + 1)
        for i in range(m):
            w = weights[i]
            v = values[i]
            for j in range(1, capacity + 1):
                if w > j:
                    continue
                dp[j] = max(dp[j], v + dp[j - w])
        return dp[capacity]
