class Solution:
    def change(
        self,
        amount: int,
        coins: list[int],
    ) -> int:
        n = amount + 1
        dp = [0] * n
        dp[0] = 1
        for coin in coins:
            for i in range(coin, n):
                dp[i] += dp[i - coin]
        return dp[amount]


if __name__ == "__main__":
    amount = 5
    coins = [1, 2, 5]
    print(Solution().change(amount, coins))
