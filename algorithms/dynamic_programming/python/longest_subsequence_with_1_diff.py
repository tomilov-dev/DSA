class SolutionRecursive:
    def search(self, arr: list[int]) -> int:
        def rec(i: int, prev: int | None = None) -> int:
            if i >= len(arr):
                return 0

            take = 0
            if prev is None or abs(arr[i] - arr[prev]) == 1:
                take = 1 + rec(i + 1, i)
            not_take = rec(i + 1, prev)
            return max(take, not_take)

        return rec(0)


class SolutionTopDown:
    def search(self, arr: list[int]) -> int:
        def rec(i: int, prev: int | None = None) -> int:
            if i >= len(arr):
                return 0

            key = (i, prev)
            if key not in mem:
                take = 0
                if prev is None or abs(arr[i] - arr[prev]) == 1:
                    take = 1 + rec(i + 1, i)
                not_take = rec(i + 1, prev)
                mem[key] = max(take, not_take)
            return mem[key]

        mem = {}
        return rec(0)


class SolutionBottomUp:
    def search(self, arr: list[int]) -> int:
        n = len(arr)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for prev in range(-1, n):
                # not_take: не берем arr[i]
                not_take = dp[i + 1][prev + 1]
                # take: берем arr[i], если можно
                take = 0
                if prev == -1 or abs(arr[i] - arr[prev]) == 1:
                    take = 1 + dp[i + 1][i + 1]
                dp[i][prev + 1] = max(take, not_take)

        return dp[0][0]


class SolutionBottomUpOptimized:
    def search(self, arr: list[int]) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            ndp = [0] * (n + 1)
            for prev in range(-1, n):
                not_take = dp[prev + 1]
                take = 0
                if prev == -1 or abs(arr[i] - arr[prev]) == 1:
                    take = 1 + dp[i + 1]
                ndp[prev + 1] = max(take, not_take)
            dp = ndp
        return dp[0]


if __name__ == "__main__":
    arr = [10, 9, 4, 5, 4, 8, 6]
    print(SolutionRecursive().search(arr))
    print(SolutionTopDown().search(arr))
    print(SolutionBottomUp().search(arr))
    print(SolutionBottomUpOptimized().search(arr))
