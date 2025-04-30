class SolutionBottomUp:
    def findMaxSum(self, arr: list[int]) -> int:
        n = len(arr)
        dp = [0] * (n + 1)
        dp[1] = arr[0]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + arr[i - 1])
        return dp[n]


class SolutionBottomUpOptimized:
    def findMaxSum(self, arr: list[int]) -> int:
        n = len(arr)
        n1 = 0
        n2 = arr[0]
        for i in range(2, n + 1):
            cur = max(n2, n1 + arr[i - 1])
            n1 = n2
            n2 = cur
        return n2


if __name__ == "__main__":
    arr = [6, 5, 5, 7, 4]
    print(SolutionBottomUp().findMaxSum(arr))
    print(SolutionBottomUpOptimized().findMaxSum(arr))
