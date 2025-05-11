class Solution:
    def maximizeTheCuts(
        self,
        n: int,
        x: int,
        y: int,
        z: int,
    ) -> int:
        sizes = [x, y, z]
        dp = [-1] * (n + 1)
        dp[0] = 0
        for size in sizes:
            for i in range(size, n + 1):
                if dp[i - size] == -1:
                    continue
                dp[i] = max(dp[i], dp[i - size] + 1)
        return max(dp[n], 0)


class SolutionTopDown:
    def maximizeTheCuts(
        self,
        n: int,
        x: int,
        y: int,
        z: int,
    ) -> int:
        def backtrack(i: int) -> int:
            if i < 0:
                return -(10**6)
            if i == 0:
                return 0
            if i in mem:
                return mem[i]

            mem[i] = 1 + max(backtrack(i - x), backtrack(i - y), backtrack(i - z))
            return mem[i]

        mem = {}
        result = backtrack(n)
        return max(result, 0)


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

    print(Solution().maximizeTheCuts(n, x, y, z))
