MAX = 10**9


class Solution:
    def coinChange(
        self,
        coins: list[int],
        amount: int,
    ) -> int:
        dp = [MAX] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] != MAX else -1
