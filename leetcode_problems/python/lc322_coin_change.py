class SolutionGreedyWrong:
    def coinChange(
        self,
        coins: list[int],
        amount: int,
    ) -> int:
        coins.sort(reverse=True)
        count = 0
        index = 0
        while amount > 0:
            if index >= len(coins):
                return -1
            if coins[index] > amount:
                index += 1
                continue
            amount -= coins[index]
            count += 1
        return count


class Solution:
    def coinChange(
        self,
        coins: list[int],
        amount: int,
    ) -> int:
        n = amount + 1
        dp = [10**5] * n
        dp[0] = 0
        for coin in coins:
            for i in range(coin, n):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != 10**5 else -1


if __name__ == "__main__":
    coins = [5, 2, 1]
    amount = 11

    print(Solution().coinChange(coins, amount))
