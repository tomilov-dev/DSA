class SolutionRecursive:
    def maximumAmount(self, arr: list[int]) -> int:
        def rec(i: int, j: int) -> int:
            if i > j:
                return 0

            left = arr[i] + min(rec(i + 2, j), rec(i + 1, j - 1))
            right = arr[j] + min(rec(i, j - 2), rec(i + 1, j - 1))
            return max(left, right)

        return rec(0, len(arr) - 1)


class SolutionTopDown:
    def maximumAmount(self, arr: list[int]) -> int:
        def rec(i: int, j: int) -> int:
            if i > j:
                return 0

            key = (i, j)
            if key not in mem:
                left = arr[i] + min(rec(i + 2, j), rec(i + 1, j - 1))
                right = arr[j] + min(rec(i, j - 2), rec(i + 1, j - 1))
                mem[key] = max(left, right)
            return mem[key]

        mem = {}
        return rec(0, len(arr) - 1)


class SolutionBottomUp:
    def maximumAmount(self, arr: list[int]) -> int:
        n = len(arr)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for gap in range(n):
            for j in range(gap, n):
                i = j - gap

                x = 0
                if (i + 2) <= j:
                    x = dp[i + 2][j]
                y = 0
                if (i + 1) <= (j - 1):
                    y = dp[i + 1][j - 1]
                z = 0
                if i <= (j - 2):
                    z = dp[i][j - 2]

                dp[i][j] = max(
                    arr[i] + min(x, y),
                    arr[j] + min(y, z),
                )

        return dp[0][n - 1]


if __name__ == "__main__":
    arr = [5, 3, 7, 10]
    print(SolutionRecursive().maximumAmount(arr))
    print(SolutionTopDown().maximumAmount(arr))
    print(SolutionBottomUp().maximumAmount(arr))
