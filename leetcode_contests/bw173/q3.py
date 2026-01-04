class Solution:
    def findMaxVal(
        self,
        n: int,
        restrictions: list[list[int]],
        diff: list[int],
    ) -> int:
        dp = [0] * n
        rst = {x: y for x, y in restrictions}
        for i in range(1, n):
            x = dp[i - 1] + diff[i - 1]
            if i in rst:
                x = min(x, rst[i])
            dp[i] = x
        for i in range(n - 2, -1, -1):
            dp[i] = min(dp[i], dp[i + 1] + diff[i])
        return max(dp)


if __name__ == "__main__":
    n = 10
    restrictions = [[3, 1], [8, 1]]
    diff = [2, 2, 3, 1, 4, 5, 1, 1, 2]

    n = 8
    restrictions = [[3, 2]]
    diff = [3, 5, 2, 4, 2, 3, 1]
    print(Solution().findMaxVal(n, restrictions, diff))
