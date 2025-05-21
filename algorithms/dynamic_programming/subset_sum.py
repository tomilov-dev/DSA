class Solution:
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
        dp = [False] * (sum + 1)
        dp[0] = True
        for num in arr:
            for i in range(sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[sum]


if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    sum = 9
    print(Solution().isSubsetSum(arr, sum))
    print(SolutionRecursive().isSubsetSum(arr, sum))
    print(SolutionTopDown().isSubsetSum(arr, sum))
    print(SolutionBottomUp().isSubsetSum(arr, sum))
