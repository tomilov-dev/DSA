import bisect


class Solution:
    def lis(self, arr: list[int]) -> int:
        n = len(arr)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if arr[i] > arr[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class SolutionOptimizedBinarySearch:
    def lis(self, arr: list[int]) -> int:
        sub = []
        for num in arr:
            pos = bisect.bisect_left(sub, num)
            if pos == len(sub):
                sub.append(num)
            else:
                sub[pos] = num
        return len(sub)


if __name__ == "__main__":
    arr = [5, 8, 3, 7, 9, 1]
    arr = [48, 37, 41, 38, 2]
    print(Solution().lis(arr))
    print(SolutionOptimizedBinarySearch().lis(arr))
