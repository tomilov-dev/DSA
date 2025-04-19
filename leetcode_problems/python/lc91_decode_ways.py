class SolutionBacktracking:
    def numDecodings(self, s: str) -> int:
        def backtrack(i: int) -> int:
            if i == len(s):
                return 1

            if s[i] == "0":
                return 0

            count = backtrack(i + 1)
            if i + 1 < len(s) and int(s[i : i + 2]) <= 26:
                count += backtrack(i + 2)

            return count

        if not s or s[0] == "0":
            return 0
        return backtrack(0)


class SolutionBacktrackingMemo:
    def numDecodings(self, s: str) -> int:
        def backtrack(i: int) -> int:
            nonlocal mem
            if i in mem:
                return mem[i]
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0

            count = backtrack(i + 1)
            if i + 1 < len(s) and int(s[i : i + 2]) <= 26:
                count += backtrack(i + 2)

            mem[i] = count
            return count

        mem = dict()
        if not s or s[0] == "0":
            return 0
        return backtrack(0)


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s.startswith("0"):
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, n):
            if s[i] != "0":
                dp[i + 1] += dp[i]
            if s[i - 1] != "0" and int(s[i - 1 : i + 1]) <= 26:
                dp[i + 1] += dp[i - 1]

        return dp[n]


if __name__ == "__main__":
    s = "111111"
    print(Solution().numDecodings(s))
