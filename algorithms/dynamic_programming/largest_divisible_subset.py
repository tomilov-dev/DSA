class SolutionRecursive:
    def largestDivisibleSubset(
        self,
        arr: list[int],
    ) -> int:
        def rec(i: int, j: int) -> int:
            """
            j - for previous
            """

            if i == len(arr):
                return 0

            take = 0
            if j == -1 or arr[i] % arr[j] == 0 or arr[j] % arr[i] == 0:
                take = 1 + rec(i + 1, i)
            not_take = rec(i + 1, j)
            return max(take, not_take)

        arr.sort()
        return rec(0, -1)


class SolutionTopDown:
    def largestDivisibleSubset(
        self,
        arr: list[int],
    ) -> int:
        def rec(i: int, j: int) -> int:
            """
            j - for previous
            """

            if i == len(arr):
                return 0

            key = (i, j)
            if key not in mem:
                take = 0
                if j == -1 or arr[i] % arr[j] == 0 or arr[j] % arr[i] == 0:
                    take = 1 + rec(i + 1, i)
                not_take = rec(i + 1, j)
                mem[key] = max(take, not_take)
            return mem[key]

        arr.sort()
        mem = {}
        return rec(0, -1)


class SolutionBottomUp:
    def largestDivisibleSubset(
        self,
        arr: list[int],
    ) -> int:
        n = len(arr)
        arr.sort()

        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if arr[i] % arr[j] == 0 or arr[j] % arr[i] == 0:
                    dp[i] = max(dp[i], 1 + dp[j])

        return dp[n - 1]


if __name__ == "__main__":
    arr = [1, 2, 3, 6]
    arr = [1, 16, 7, 8, 4]
    arr = [2, 4, 3, 8]

    print(SolutionRecursive().largestDivisibleSubset(arr))
    print(SolutionTopDown().largestDivisibleSubset(arr))
    print(SolutionBottomUp().largestDivisibleSubset(arr))
