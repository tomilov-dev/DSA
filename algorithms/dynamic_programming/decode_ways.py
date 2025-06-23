class Solution:
    def countWays(self, digits: str) -> int:
        n = len(digits)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, n):
            if digits[i] != "0":
                dp[i + 1] += dp[i]
            if digits[i - 1] != "0" and int(digits[i - 1 : i + 1]) <= 26:
                dp[i + 1] += dp[i - 1]
        return dp[n]


class SolutionRecursive:
    def countWays(self, digits: str) -> int:
        def rec(i: int) -> int:
            if i >= len(digits):
                return 1

            ways = 0
            if digits[i] != "0":
                ways += rec(i + 1)

            num = int(digits[i : i + 2])
            if 10 <= num <= 26:
                ways += rec(i + 2)
            return ways

        return rec(0)


class SolutionTopDown:
    def countWays(self, digits: str) -> int:
        def rec(i: int) -> int:
            if i >= len(digits):
                return 1

            if i not in mem:
                ways = 0
                if digits[i] != "0":
                    ways += rec(i + 1)

                num = int(digits[i : i + 2])
                if 10 <= num <= 26:
                    ways += rec(i + 2)
                mem[i] = ways
            return mem[i]

        mem = {}
        return rec(0)


class SolutionBottomUp:
    def countWays(self, digits: str) -> int:
        n = len(digits)
        dp = [0] * (n + 2)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if digits[i] != "0":
                dp[i] += dp[i + 1]
            num = int(digits[i : i + 2])
            if 10 <= num <= 26:
                dp[i] += dp[i + 2]
        return dp[0]


class SolutionBottomUpOptimized:
    def countWays(self, digits: str) -> int:
        n = len(digits)
        n1 = 0
        n2 = 1

        dp = [0] * (n + 2)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            cur = 0
            if digits[i] != "0":
                cur += n2
            num = int(digits[i : i + 2])
            if 10 <= num <= 26:
                cur += n1

            n1 = n2
            n2 = cur

        return cur


if __name__ == "__main__":
    digits = "123"
    digits = "1234"
    print(Solution().countWays(digits))
    print(SolutionRecursive().countWays(digits))
    print(SolutionTopDown().countWays(digits))
    print(SolutionBottomUp().countWays(digits))
    print(SolutionBottomUpOptimized().countWays(digits))
