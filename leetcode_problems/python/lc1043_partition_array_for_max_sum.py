class Solution:
    def maxSumAfterPartitioning(
        self,
        arr: list[int],
        K: int,
    ) -> int:
        dp = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            curMax = 0
            for k in range(1, min(K, i) + 1):
                curMax = max(curMax, arr[i - k])
                dp[i] = max(dp[i], dp[i - k] + curMax * k)

        return dp[len(arr)]


if __name__ == "__main__":
    arr = [1, 15, 7, 9, 2, 5, 10]
    k = 3
    print(Solution().maxSumAfterPartitioning(arr, k))
