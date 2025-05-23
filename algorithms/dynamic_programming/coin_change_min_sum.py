class Solution:
    def minCoins(
        self,
        coins: list[int],
        sum: int,
    ) -> int:
        dp = [10**5] * (sum + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, sum + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[sum]


class SolutionRecursive:
    def minCoins(
        self,
        coins: list[int],
        sum: int,
    ) -> int:
        def rec(i: int, sm: int, used: int = 0) -> int:
            if sm == 0:
                return used
            if sm < 0 or i >= len(coins):
                return 10**6

            return min(
                rec(i, sm - coins[i], used + 1),
                rec(i + 1, sm, used),
            )

        return rec(0, sum)


class SolutionTopDown:
    def minCoins(
        self,
        coins: list[int],
        sum: int,
    ) -> int:
        def rec(i: int, sm: int, used: int = 0) -> int:
            if sm == 0:
                return used
            if sm < 0 or i >= len(coins):
                return 10**6

            key = (i, sm)
            if key not in mem:
                mem[key] = min(
                    rec(i, sm - coins[i], used + 1),
                    rec(i + 1, sm, used),
                )
            return mem[key]

        mem = {}
        return rec(0, sum)


class SolutionBottomUp:
    def minCoins(
        self,
        coins: list[int],
        sum: int,
    ) -> int:
        dp = [10**6] * (sum + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, sum + 1):
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[sum]


if __name__ == "__main__":
    coins = [25, 10, 5]
    sum = 30
    print(Solution().minCoins(coins, sum))
    print(SolutionRecursive().minCoins(coins, sum))
    print(SolutionTopDown().minCoins(coins, sum))
    print(SolutionBottomUp().minCoins(coins, sum))
