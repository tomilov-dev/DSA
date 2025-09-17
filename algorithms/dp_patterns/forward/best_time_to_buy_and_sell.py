class SolutionBottomUp:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        min_price = prices[0]
        max_profit = 0
        for i in range(1, n):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])
        return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    sol = SolutionBottomUp()
    print(sol.maxProfit(prices))
