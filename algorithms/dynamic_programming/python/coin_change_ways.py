class Solution:
    def count(
        self,
        coins: list[int],
        sum: int,
    ) -> int:
        dp = [0] * (sum + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, sum + 1):
                dp[i] += dp[i - coin]
        return dp[sum]


class SolutionRecursive:
    def count(
        self,
        coins: list[int],
        sum: int,
    ) -> int:
        def rec(i: int, sm: int) -> int:
            if sm == 0:
                return 1
            if sm < 0 or i >= len(coins):
                return 0
            return rec(i, sm - coins[i]) + rec(i + 1, sm)

        return rec(0, sum)


class SolutionTopDown:
    def count(
        self,
        coins: list[int],
        sum: int,
    ) -> int:
        def rec(i: int, sm: int) -> int:
            if sm == 0:
                return 1
            if sm < 0 or i >= len(coins):
                return 0

            key = (i, sm)
            if key not in mem:
                mem[key] = rec(i, sm - coins[i]) + rec(i + 1, sm)
            return mem[key]

        mem = {}
        return rec(0, sum)


class SolutionBottomUp:
    def count(
        self,
        coins: list[int],
        sum: int,
    ) -> int:
        dp = [0] * (sum + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, sum + 1):
                dp[i] += dp[i - coin]
        return dp[sum]


if __name__ == "__main__":
    coins = [2, 5, 3, 6]
    sum = 10

    # coins = [1, 2, 3]
    # sum = 4
    print(Solution().count(coins, sum))
    print(SolutionRecursive().count(coins, sum))
    print(SolutionTopDown().count(coins, sum))
    print(SolutionBottomUp().count(coins, sum))
