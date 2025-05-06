class Solution:
    def largestDivisibleSubset(
        self,
        arr: list[int],
    ) -> int:
        arr.sort()
        n = len(arr)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if arr[i] % arr[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return dp[n - 1]


class SolutionFull:
    def largestDivisibleSubset(
        self,
        arr: list[int],
    ) -> list[int]:
        arr.sort()
        n = len(arr)

        dp = [1] * n
        parent = [-1] * n

        max_size = 1
        last_index = 0
        for i in range(1, n):
            for j in range(i):
                if arr[i] % arr[j] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parent[i] = j

            if dp[i] > max_size:
                max_size = dp[i]
                last_index = i

        res = []
        while last_index >= 0:
            res.append(arr[last_index])
            last_index = parent[last_index]

        res.reverse()
        return res


if __name__ == "__main__":
    arr = [1, 2, 3, 6]
    print(Solution().largestDivisibleSubset(arr))
