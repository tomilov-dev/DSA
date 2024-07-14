class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        if len(cost) == 0:
            return 0
        if len(cost) == 1:
            return cost[-1]
        if len(cost) == 2:
            return min(cost[0], cost[1])

        dp = [0] * (len(cost) + 1)
        cost.append(0)

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(dp)):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]

        return dp[-1]


if __name__ == "__main__":
    # cost = [10, 15, 20]
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(Solution().minCostClimbingStairs(cost))
