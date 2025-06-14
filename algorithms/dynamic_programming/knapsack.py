class SolutionRecursive:
    def knapsack(
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
                take = profits[i] + rec(i + 1, w - weights[i])
            not_take = rec(i + 1, w)
            return max(take, not_take)

        n = len(profits)
        return rec(0, total_weight)


class SolutionTopDown:
    def knapsack(
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
                    take = profits[i] + rec(i + 1, w - weights[i])
                not_take = rec(i + 1, w)
                mem[key] = max(take, not_take)
            return mem[key]

        n = len(profits)
        mem = {}
        return rec(0, total_weight)


class SolutionBottomUp:
    def knapsack(
        self,
        total_weight: int,
        profits: list[int],
        weights: list[int],
    ) -> int:
        """
        Отличие задачи от unbound knapsack в этой строчке кода:
        `dp[i][j] = max(dp[i - 1][j], p + dp[i - 1][j - w])`
        Мы используем `dp[i - 1][j - w]` заместо `dp[i][j - w]
        Потому что не можем переиспользовать текущий i-й предмет
        """

        n = len(profits)
        dp = [[0] * (total_weight + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            p = profits[i - 1]
            w = weights[i - 1]
            for j in range(1, total_weight + 1):
                if w <= j:
                    # pick item
                    dp[i][j] = max(dp[i - 1][j], p + dp[i - 1][j - w])
                else:
                    # not pick item
                    dp[i][j] = dp[i - 1][j]

        return dp[n][w]


class SolutionBottomUpOptimized:
    def knapsack(
        self,
        total_weight: int,
        profits: list[int],
        weights: list[int],
    ) -> int:
        """
        Отличие задачи от unbound knapsack в том, что мы обходим по весу в обратном порядке
        То есть в этой строчке `for j in range(total_weight, w - 1, -1):`
        Именно здесь решения отличаются - мы идем в обратном порядке от большего к меньшему
        В unbound knapsack используется `for j in range(w, total_weight + 1):`
        """

        n = len(profits)
        dp = [0] * (total_weight + 1)
        for i in range(n):
            w = weights[i]
            p = profits[i]
            for j in range(total_weight, w - 1, -1):
                dp[j] = max(dp[j], p + dp[j - w])
        return dp[n]


if __name__ == "__main__":
    w = 4
    val = [1, 2, 3]
    wt = [4, 5, 1]

    print(SolutionRecursive().knapsack(w, val, wt))
    print(SolutionTopDown().knapsack(w, val, wt))
    print(SolutionBottomUp().knapsack(w, val, wt))
    print(SolutionBottomUpOptimized().knapsack(w, val, wt))
