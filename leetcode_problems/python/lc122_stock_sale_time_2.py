class SolutionGreedy:
    def maxProfit(self, prices: list[int]) -> int:
        mp = prices[0]
        sm = 0
        for i in range(1, len(prices)):
            sm += max(0, prices[i] - mp)
            mp = prices[i]
        return sm


class SolutionGreedy2:
    def maxProfit(self, prices: list[int]) -> int:
        sm = 0
        for i in range(1, len(prices)):
            sm += max(0, prices[i] - prices[i - 1])
        return sm


class SolutionGreedy3:
    def maxProfit(self, prices: list[int]) -> int:
        return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))


class SolutionDPBottomUp:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [0] * n
        mp = prices[0]
        for i in range(1, n):
            dp[i] = max(0, prices[i] - mp)
            mp = prices[i]
        return sum(dp)


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(SolutionDPBottomUp().maxProfit(prices))
