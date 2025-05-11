class Solution:
    def minJumps(self, arr: list[int]) -> int:
        n = len(arr)
        dp = [10**5] * n
        dp[0] = 0
        for i in range(1, n):
            jumps = arr[i - 1]
            for j in range(i, min(i + jumps, n)):
                dp[j] = min(dp[j], dp[i - 1] + 1)
        return -1 if dp[n - 1] == 10**5 else dp[n - 1]


if __name__ == "__main__":
    arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    arr = [1, 4, 3, 2, 6, 7]
    arr = [0, 10, 20]
    print(Solution().minJumps(arr))
