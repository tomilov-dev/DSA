class SolutionBottomUpFirst:
    def cutRod(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [0] + prices[:]
        for i in range(1, n + 1):
            for j in range(i, -1, -1):
                dp[i] = max(dp[i], dp[j] + dp[i - j])
        return dp[n]


class SolutionBottomUpCorrect:
    def cutRod(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] = max(dp[i], prices[j - 1] + dp[i - j])
        return dp[n]


if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    prices = [3, 5, 8, 9, 10, 17, 17, 20]
    prices = [1, 10, 3, 1, 3, 1, 5, 9]
    print(SolutionBottomUpFirst().cutRod(prices))
    print(SolutionBottomUpCorrect().cutRod(prices))
