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


if __name__ == "__main__":
    coins = [2, 5, 3, 6]
    sum = 10

    # coins = [1, 2, 3]
    # sum = 4
    print(Solution().count(coins, sum))
