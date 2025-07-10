class SolutionRecursive:
    def cutRod(self, prices: list[int]) -> int:
        def rec(l: int, i: int, sum: int = 0) -> int:
            if l < 0:
                return -(10**6)
            if i >= n:
                return 0
            if l == 0:
                return sum

            return max(
                rec(l - (i + 1), i, sum + prices[i]),
                rec(l, i + 1, sum),
            )

        n = len(prices)
        return rec(n, 0)


class SolutionTopDown:
    def cutRod(self, prices: list[int]) -> int:
        def rec(l: int, i: int, sum: int = 0) -> int:
            if l < 0:
                return -(10**6)
            if i >= n:
                return 0
            if l == 0:
                return sum

            key = (i, sum)
            if key not in mem:
                mem[key] = max(
                    rec(l - (i + 1), i, sum + prices[i]),
                    rec(l, i + 1, sum),
                )
            return mem[key]

        mem = {}
        n = len(prices)
        return rec(n, 0)


class SolutionTopDownOptimized:
    def cutRod(self, prices: list[int]) -> int:
        def rec(l: int, i: int) -> int:
            if l < 0:
                return -(10**6)
            if i >= n:
                return 0
            if l == 0:
                return 0

            key = (i, l)
            if key not in mem:
                mem[key] = max(
                    prices[i] + rec(l - (i + 1), i),
                    rec(l, i + 1),
                )
            return mem[key]

        mem = {}
        n = len(prices)
        return rec(n, 0)


class SolutionBottomUp:
    def cutRod(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(i, n + 1):
                dp[i][j] = max(
                    dp[i][j],
                    dp[i - 1][j],
                    dp[i][j - i] + prices[i - 1],
                )

        return dp[n][n]


class SolutionBottomUpOptimized:
    def cutRod(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] = max(dp[i], dp[i - j] + prices[j - 1])
        return dp[n]


if __name__ == "__main__":
    prices = [1, 5, 8, 9, 10, 17, 17, 20]
    prices = [3, 5, 8, 9, 10, 17, 17, 20]
    prices = [1, 10, 3, 1, 3, 1, 5, 9]
    print(SolutionRecursive().cutRod(prices))
    print(SolutionTopDown().cutRod(prices))
    print(SolutionTopDownOptimized().cutRod(prices))
    print(SolutionBottomUp().cutRod(prices))
    print(SolutionBottomUpOptimized().cutRod(prices))
