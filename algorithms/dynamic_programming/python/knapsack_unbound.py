class SolutionRecursive:
    def knapSack(
        self,
        total_weight: int,
        profits: list[int],
        weights: list[int],
    ) -> int:
        def rec(i: int, w: int) -> int:
            if i >= n:
                return 0

            take = 0
            if w >= weights[i]:
                take = profits[i] + rec(i, w - weights[i])
            not_take = rec(i + 1, w)
            return max(take, not_take)

        n = len(profits)
        return rec(0, total_weight)


class SolutionTopDown:
    def knapSack(
        self,
        total_weight: int,
        profits: list[int],
        weights: list[int],
    ) -> int:
        def rec(i: int, w: int) -> int:
            if i >= n:
                return 0

            key = (i, w)
            if key not in mem:
                take = 0
                if w >= weights[i]:
                    take = profits[i] + rec(i, w - weights[i])
                not_take = rec(i + 1, w)
                mem[key] = max(take, not_take)
            return mem[key]

        n = len(profits)
        mem = {}
        return rec(0, total_weight)


class SolutionBottomUp:
    def knapSack(
        self,
        total_weight: int,
        profits: list[int],
        weights: list[int],
    ) -> int:
        """
        Отличие задачи от unbound knapsack в этой строчке кода:
        `dp[i][j] = max(dp[i - 1][j], p + dp[i][j - w])`
        Мы используем `dp[i][j - w]` заместо `dp[i - 1][j - w]
        Потому что можем переиспользовать текущий i-й предмет
        """

        n = len(val)
        dp = [[0] * (total_weight + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            w = weights[i - 1]
            p = profits[i - 1]
            for j in range(1, total_weight + 1):
                if w <= j:
                    # pick item
                    dp[i][j] = max(dp[i - 1][j], p + dp[i][j - w])
                else:
                    # not pick item
                    dp[i][j] = dp[i - 1][j]
        return dp[n][total_weight]


class SolutionBottomUpOptimized:
    def knapSack(
        self,
        total_weight: int,
        profits: list[int],
        weights: list[int],
    ) -> int:
        """
        Отличие задачи от knapsack в том, что мы обходим по весу в обратном порядке
        То есть в этой строчке `for j in range(w, total_weight + 1):`
        Именно здесь решения отличаются - мы идем в прямом порядке от меньшего к большему
        В knapsack используется `for j in range(total_weight, w - 1, -1):`
        """

        n = len(val)
        dp = [0] * (total_weight + 1)
        for i in range(n):
            w = weights[i]
            p = profits[i]
            for j in range(w, total_weight + 1):
                dp[j] = max(dp[j], p + dp[j - w])
        return dp[total_weight]


if __name__ == "__main__":
    val = [6, 1, 7, 7]
    wt = [1, 3, 4, 5]
    w = 8

    # print(Solution().knapSack(w, val, wt))
    # print(SolutionOptimized().knapSack(w, val, wt))
    print(SolutionRecursive().knapSack(w, val, wt))
    print(SolutionTopDown().knapSack(w, val, wt))
    print(SolutionBottomUp().knapSack(w, val, wt))
    print(SolutionBottomUpOptimized().knapSack(w, val, wt))
