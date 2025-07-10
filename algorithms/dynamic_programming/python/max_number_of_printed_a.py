class SolutionRecursive:
    def optimalKeys(self, n: int) -> int:
        def rec(i: int) -> int:
            if i < 7:
                return i

            maxi = 0
            for j in range(i - 3, 0, -1):
                maxi = max(maxi, rec(j) * (i - j - 1))
            return maxi

        return rec(n)


class SolutionTopDown:
    def optimalKeys(self, n: int) -> int:
        def rec(i: int) -> int:
            if i < 7:
                return i

            if i not in mem:
                mem[i] = 0
                for j in range(i - 3, 0, -1):
                    mem[i] = max(mem[i], rec(j) * (i - j - 1))
            return mem[i]

        mem = dict()
        return rec(n)


class SolutionBottomUp:
    def optimalKeys(self, n: int) -> int:
        if n < 7:
            return n

        dp = [0] * (n + 1)
        for i in range(7):
            dp[i] = i

        for i in range(7, n + 1):
            for j in range(i - 3, 0, -1):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
        return dp[n]


class SolutionBottomUpOptimized:
    def optimalKeys(self, n: int) -> int:
        if n < 7:
            return n

        dp = [0] * (n + 1)
        for i in range(7):
            dp[i] = i

        for i in range(7, n + 1):
            dp[i] = max(
                2 * dp[i - 3],
                3 * dp[i - 4],
                4 * dp[i - 5],
            )
        return dp[n]


if __name__ == "__main__":
    n = 7
    print(SolutionRecursive().optimalKeys(n))
    print(SolutionTopDown().optimalKeys(n))
    print(SolutionBottomUp().optimalKeys(n))
    print(SolutionBottomUpOptimized().optimalKeys(n))
