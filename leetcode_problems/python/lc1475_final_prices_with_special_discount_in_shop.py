class Solution:
    def finalPrices(
        self,
        prices: list[int],
    ) -> list[int]:
        res = [None for _ in range(len(prices))]
        stack = []
        for index, price in enumerate(prices):
            while stack and stack[-1][1] >= price:
                li, lp = stack.pop()
                res[li] = lp - price
            stack.append((index, price))

        while stack:
            li, lp = stack.pop()
            res[li] = lp

        return res


if __name__ == "__main__":
    prices = [8, 4, 6, 2, 3]
    print(Solution().finalPrices(prices))
