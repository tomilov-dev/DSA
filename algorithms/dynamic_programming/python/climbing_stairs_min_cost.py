class SolutionRecursive:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        def rec(i: int) -> int:
            if i == 0:
                return cost[0]
            if i == 1:
                return cost[1]
            return cost[i] + min(rec(i - 1), rec(i - 2))

        n = len(cost)
        return min(rec(n - 1), rec(n - 2))


class SolutionTopDown:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        def rec(i: int) -> int:
            if i == 0:
                return cost[0]
            if i == 1:
                return cost[1]
            if i not in mem:
                mem[i] = cost[i] + min(rec(i - 1), rec(i - 2))
            return mem[i]

        n = len(cost)
        mem = {}
        return min(rec(n - 1), rec(n - 2))


class SolutionBottomUp:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[n - 1], dp[n - 2])


class SolutionBottomUpOptimized:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        n1 = cost[0]
        n2 = cost[1]
        for i in range(2, n):
            n3 = cost[i] + min(n1, n2)
            n1 = n2
            n2 = n3
        return min(n1, n2)


if __name__ == "__main__":
    cost = [10, 15, 20]
    # cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]

    print(SolutionRecursive().minCostClimbingStairs(cost))
    print(SolutionTopDown().minCostClimbingStairs(cost))
    print(SolutionBottomUp().minCostClimbingStairs(cost))
    print(SolutionBottomUpOptimized().minCostClimbingStairs(cost))
