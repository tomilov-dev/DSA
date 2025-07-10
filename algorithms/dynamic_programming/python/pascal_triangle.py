class SolutionRecursive:
    def nthRowOfPascalTriangle(self, n: int) -> list[int]:
        def rec(i: int) -> list[int]:
            if i == 1:
                return [1]

            prev = rec(i - 1)
            n = len(prev) + 1
            cur = [0] * n
            for i in range(n):
                if i == 0:
                    cur[i] = prev[0]
                elif i == n - 1:
                    cur[i] = prev[-1]
                else:
                    cur[i] = prev[i] + prev[i - 1]
            return cur

        return rec(n)


class SolutionRecursiveRefactor:
    def nthRowOfPascalTriangle(self, n: int) -> list[int]:
        def rec(i: int) -> list[int]:
            if i == 1:
                return [0, 1, 0]

            prev = rec(i - 1)
            n = len(prev)
            cur = [0] * n
            for i in range(n):
                cur[i] = prev[i - 1] + prev[i]
            return cur + [0]

        ## Here we add extra 0s to avoid if-else statements
        return rec(n)[1:-1]


class SolutionTopDown:
    def nthRowOfPascalTriangle(self, n: int) -> list[int]:
        def rec(i: int) -> list[int]:
            if i == 1:
                return [1]

            if i not in mem:
                prev = rec(i - 1)
                n = len(prev) + 1
                cur = [0] * n
                for i in range(n):
                    if i == 0:
                        cur[i] = prev[0]
                    elif i == n - 1:
                        cur[i] = prev[-1]
                    else:
                        cur[i] = prev[i] + prev[i - 1]
                mem[i] = cur
            return mem[i]

        mem = {}
        return rec(n)


class SolutionBottomUp:
    def nthRowOfPascalTriangle(self, n: int) -> list[int]:
        dp = [[0] * (n + 2) for _ in range(n)]
        dp[0][1] = 1
        for i in range(1, n):
            for j in range(i + 2):
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
        return dp[n - 1][1:-1]


class SolutionBottomUpOptimized:
    def nthRowOfPascalTriangle(self, n: int) -> list[int]:
        dp = [0] * (n + 2)
        dp[1] = 1
        ndp = [0] * (n + 2)
        for i in range(1, n):
            for j in range(i + 2):
                ndp[j] = dp[j] + dp[j - 1]
            dp, ndp = ndp, dp
        return dp[1:-1]


if __name__ == "__main__":
    n = 11
    print(SolutionRecursive().nthRowOfPascalTriangle(n))
    print(SolutionRecursiveRefactor().nthRowOfPascalTriangle(n))
    print(SolutionTopDown().nthRowOfPascalTriangle(n))
    print(SolutionBottomUp().nthRowOfPascalTriangle(n))
    print(SolutionBottomUpOptimized().nthRowOfPascalTriangle(n))
