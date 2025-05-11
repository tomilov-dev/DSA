class SolutionRecursive:
    def equalPartition(self, arr: list[int]) -> bool:
        def rec(n: int, sm: int) -> bool:
            if sm == 0:
                return True
            if n <= 0:
                return False

            if arr[n - 1] > sm:
                return rec(n - 1, sm)
            return rec(n - 1, sm) or rec(n - 1, sm - arr[n - 1])

        sm = sum(arr)
        if sm % 2 != 0:
            return False
        return rec(len(arr), sm // 2)


class SolutionTopDown:
    def equalPartition(self, arr: list[int]) -> bool:
        def rec(n: int, sm: int) -> bool:
            if sm == 0:
                return True
            if n <= 0:
                return False

            if n not in mem:
                key = (n - 1, sm)
                if arr[n - 1] > sm:
                    mem[key] = rec(n - 1, sm)
                else:
                    mem[key] = rec(n - 1, sm) or rec(n - 1, sm - arr[n - 1])
            return mem[key]

        sm = sum(arr)
        if sm % 2 != 0:
            return False
        mem = {}
        return rec(len(arr), sm // 2)


class SolutionBottomUp:
    def equalPartition(self, arr: list[int]) -> bool:
        n = len(arr)
        sm = sum(arr)
        if sm % 2 != 0:
            return False

        sm //= 2
        dp = [[False] * (sm + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, sm + 1):
                if j < arr[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                    continue
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]

        return dp[n][sm]


class SolutionBottomUpOptimized:
    def equalPartition(self, arr: list[int]) -> bool:
        n = len(arr)
        sm = sum(arr)
        if sm % 2 != 0:
            return False

        sm //= 2
        dp = [False] * (sm + 1)
        ndp = [False] * (sm + 1)
        for i in range(1, n + 1):
            dp[0] = True
            for j in range(1, sm + 1):
                if j < arr[i - 1]:
                    ndp[j] = dp[j]
                    continue
                ndp[j] = dp[j] or dp[j - arr[i - 1]]
            dp, ndp = ndp, dp
        return dp[sm]


if __name__ == "__main__":
    arr = [1, 5, 11, 5]
    arr = [1, 3, 5]
    arr = [6, 2, 3, 10, 2, 9, 10, 2]
    print(SolutionRecursive().equalPartition(arr))
    print(SolutionTopDown().equalPartition(arr))
    print(SolutionBottomUp().equalPartition(arr))
    print(SolutionBottomUpOptimized().equalPartition(arr))
