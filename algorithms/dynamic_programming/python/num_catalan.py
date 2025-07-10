class SolutionBinomial:
    def binom(self, n: int, k: int):
        res = 1
        if k > n - k:
            k = n - k
        for i in range(k):
            res *= n - i
            res //= i + 1
        return res

    def findCatalan(self, n: int) -> int:
        cat = self.binom(n * 2, n)
        return cat // (n + 1)


class SolutionRecursive:
    def findCatalan(self, n: int) -> int:
        def rec(i: int) -> int:
            if i == 0:
                return 1
            if i == 1:
                return 1

            sum = 0
            for j in range(i):
                sum += rec(j) * rec(i - j - 1)
            return sum

        return rec(n)


class SolutionTopDown:
    def findCatalan(self, n: int) -> int:
        def rec(i: int) -> int:
            if i == 0:
                return 1
            if i == 1:
                return 1

            if i not in mem:
                mem[i] = 0
                for j in range(i):
                    mem[i] += rec(j) * rec(i - j - 1)
            return mem[i]

        mem = {}
        return rec(n)


class SolutionBottomUp:
    def findCatalan(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]


if __name__ == "__main__":
    n = 6
    print(SolutionRecursive().findCatalan(n))
    print(SolutionTopDown().findCatalan(n))
    print(SolutionBottomUp().findCatalan(n))
    print(SolutionBinomial().findCatalan(n))
