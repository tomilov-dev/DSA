class SolutionRecursive:
    def maximizeTheCuts(
        self,
        n: int,
        x: int,
        y: int,
        z: int,
    ) -> int:
        def rec(i: int) -> int:
            if i == 0:
                return 0
            if i < 0:
                return -(10**5)
            return 1 + max(rec(i - x), rec(i - y), rec(i - z))

        return max(0, rec(n))


class SolutionTopDown:
    def maximizeTheCuts(
        self,
        n: int,
        x: int,
        y: int,
        z: int,
    ) -> int:
        def rec(i: int) -> int:
            if i < 0:
                return -(10**5)
            if i == 0:
                return 0
            if i not in mem:
                mem[i] = 1 + max(rec(i - x), rec(i - y), rec(i - z))
            return mem[i]

        mem = {}
        return max(0, rec(n))


class SolutionBottomUp:
    def maximizeTheCuts(
        self,
        n: int,
        x: int,
        y: int,
        z: int,
    ) -> int:
        dp = [-1] * (n + 1)
        dp[0] = 0
        sizes = [x, y, z]
        for size in sizes:
            for i in range(size, n + 1):
                if dp[i - size] == -1:
                    continue
                dp[i] = max(dp[i], 1 + dp[i - size])
        return max(0, dp[n])


if __name__ == "__main__":
    n = 4
    x = 2
    y = 1
    z = 1

    n = 5
    x = 5
    y = 3
    z = 2

    n = 7
    x = 8
    y = 9
    z = 10

    n = 7
    x = 5
    y = 5
    z = 2

    print(SolutionRecursive().maximizeTheCuts(n, x, y, z))
    print(SolutionTopDown().maximizeTheCuts(n, x, y, z))
    print(SolutionBottomUp().maximizeTheCuts(n, x, y, z))
