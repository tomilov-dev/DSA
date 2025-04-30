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


if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    sum = 9
    print(Solution().isSubsetSum(arr, sum))
