class Solution:
    def count(self, n: int) -> int:
        if n < 3:
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n - 2]


class SolutionTopDown:
    def count(self, n: int) -> int:
        def backtrack(i: int) -> int:
            if i not in mem:
                mem[i] = 0
                for j in range(0, i):
                    mem[i] += backtrack(j) * backtrack(i - j - 1)
            return mem[i]

        if n < 3:
            return 0

        mem = {0: 1, 1: 1}
        backtrack(n)
        return mem[n - 2]


class SolutionBinomial:
    def binom(self, n: int, k: int):
        res = 1
        if k > n - k:
            k = n - k
        for i in range(k):
            res *= n - i
            res //= i + 1
        return res

    def count(self, n: int) -> int:
        n -= 2
        cat = self.binom(n * 2, n)
        return cat // (n + 1)


if __name__ == "__main__":
    n = 6
    print(Solution().count(n))
    print(SolutionTopDown().count(n))
    print(SolutionBinomial().count(n))
