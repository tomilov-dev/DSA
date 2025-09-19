class SolutionRecursive:
    def numDecodings(self, s: str) -> int:
        def rec(i: int) -> int:
            if i == n:
                return 1
            if s[i] == "0":
                return 0

            count = rec(i + 1)
            if i + 1 < n and 10 <= int(s[i : i + 2]) <= 26:
                count += rec(i + 2)
            return count

        n = len(s)
        return rec(0)


class SolutionTopDown:
    def numDecodings(self, s: str) -> int:
        def rec(i: int) -> int:
            if i == n:
                return 1
            if s[i] == "0":
                return 0

            key = i
            if key not in mem:
                count = rec(i + 1)
                if i + 1 < n and 10 <= int(s[i : i + 2]) <= 26:
                    count += rec(i + 2)
                mem[key] = count
            return mem[key]

        n = len(s)
        mem = {}
        return rec(0)


class SolutionBottomUp:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
                continue

            dp[i] = dp[i + 1]
            if i + 1 < n and 10 <= int(s[i : i + 2]) <= 26:
                dp[i] += dp[i + 2]
        return dp[0]


if __name__ == "__main__":
    s = "226"
    # s = "12"
    # s = "06"
    sol = SolutionBottomUp()
    print(sol.numDecodings(s))
