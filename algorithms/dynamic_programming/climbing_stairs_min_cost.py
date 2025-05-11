class Solution:
    def minCostClimbingStairs(
        self,
        cost: list[int],
    ) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
        return min(dp[n - 1], dp[n - 2])


class SolutionOptimized:
    def minCostClimbingStairs(
        self,
        cost: list[int],
    ) -> int:
        n = len(cost)
        n1 = cost[0]
        n2 = cost[1]
        for i in range(2, n):
            cur = cost[i] + min(n1, n2)
            n1 = n2
            n2 = cur
        return min(n1, n2)


class SolutionTopDown:
    def minCostClimbingStairs(
        self,
        cost: list[int],
    ) -> int:
        def backtrack(i: int) -> int:
            if i not in mem:
                mem[i] = cost[i] + min(backtrack(i - 1), backtrack(i - 2))
            return mem[i]

        n = len(cost)
        mem = {0: cost[0], 1: cost[1]}
        backtrack(n - 1)
        return min(mem[n - 1], mem[n - 2])


if __name__ == "__main__":
    cost = [10, 15, 20]
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(Solution().minCostClimbingStairs(cost))
    print(SolutionOptimized().minCostClimbingStairs(cost))
    print(SolutionTopDown().minCostClimbingStairs(cost))
