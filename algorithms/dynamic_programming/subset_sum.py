class SolutionRecursive:
    def isSubsetSum(
        self,
        arr: list[int],
        sum: int,
    ) -> bool:
        def rec(i: int, sum: int) -> bool:
            if sum < 0:
                return False
            if sum == 0:
                return True
            if i >= len(arr):
                return False
            return rec(i + 1, sum) or rec(i + 1, sum - arr[i])

        return rec(0, sum)


class SolutionTopDown:
    def isSubsetSum(
        self,
        arr: list[int],
        sum: int,
    ) -> bool:
        def rec(i: int, sum: int) -> bool:
            if sum < 0:
                return False
            if sum == 0:
                return True
            if i >= len(arr):
                return False

            key = (i, sum)
            if key not in mem:
                mem[key] = rec(i + 1, sum) or rec(i + 1, sum - arr[i])
            return mem[key]

        mem = {}
        return rec(0, sum)


class SolutionBottomUp:
    def isSubsetSum(
        self,
        arr: list[int],
        sum: int,
    ) -> bool:
        n = len(arr)
        dp = [[False] * (sum + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, sum + 1):
                if j < arr[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
        return dp[n][sum]


class SolutionBottomUpOptimized:
    def isSubsetSum(
        self,
        arr: list[int],
        sum: int,
    ) -> bool:
        n = len(arr)
        dp = [False] * (sum + 1)
        ndp = [False] * (sum + 1)

        dp[0] = True
        for i in range(1, n + 1):
            for j in range(sum + 1):
                if j < arr[i - 1]:
                    ndp[j] = dp[j]
                else:
                    ndp[j] = dp[j] or dp[j - arr[i - 1]]
            dp, ndp = ndp, dp

        return dp[sum]


class SolutionBottomUpSuperOptimized:
    def isSubsetSum(
        self,
        arr: list[int],
        sum: int,
    ) -> bool:
        dp = [False] * (sum + 1)
        dp[0] = True
        for num in arr:
            for i in range(sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[sum]


if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    sum = 9
    print(SolutionRecursive().isSubsetSum(arr, sum))
    print(SolutionTopDown().isSubsetSum(arr, sum))
    print(SolutionBottomUp().isSubsetSum(arr, sum))
    print(SolutionBottomUpOptimized().isSubsetSum(arr, sum))
    print(SolutionBottomUpSuperOptimized().isSubsetSum(arr, sum))
