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


if __name__ == "__main__":
    coins = [25, 10, 5]
    sum = 30
    print(Solution().minCoins(coins, sum))
