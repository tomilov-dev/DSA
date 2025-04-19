class Solution:
    def countBits(self, n: int) -> list[int]:
        res = [0]
        for i in range(1, n + 1):
            res.append(res[i >> 1] + i % 2)
        return res


class SolutionDPBottomUp:
    def countBits(self, n: int) -> list[int]:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i // 2] + i % 2
        return dp


if __name__ == "__main__":
    n = 5
    res = Solution().countBits(n)
    print(res)
