class SolutionRecursive:
    def isMatch(self, s: str, p: str) -> bool:
        def rec(i: int, j: int) -> bool:
            if i >= n and j >= m:
                return True
            if j >= m:
                return False
            if i >= n:
                return all(x == "*" for x in p[j:])

            if p[j] == "*":
                for k in range(i, n + 1):
                    if rec(k, j + 1):
                        return True
                return False
            elif p[j] == "?":
                return rec(i + 1, j + 1)
            else:
                return s[i] == p[j] and rec(i + 1, j + 1)

        n = len(s)
        m = len(p)
        return rec(0, 0)


class SolutionTopDown:
    def isMatch(self, s: str, p: str) -> bool:
        def rec(i: int, j: int) -> bool:
            if i >= n and j >= m:
                return True
            if j >= m:
                return False
            if i >= n:
                return all(x == "*" for x in p[j:])

            key = (i, j)
            if key not in mem:
                if p[j] == "*":
                    mem[key] = False
                    for k in range(i, n + 1):
                        if rec(k, j + 1):
                            mem[key] = True
                            break
                elif p[j] == "?":
                    mem[key] = rec(i + 1, j + 1)
                else:
                    mem[key] = s[i] == p[j] and rec(i + 1, j + 1)
            return mem[key]

        n = len(s)
        m = len(p)
        mem = {}
        return rec(0, 0)


class SolutionBottomUp:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            if p[i - 1] == "*":
                dp[i][0] = dp[i - 1][0]
            else:
                break

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pat = p[i - 1]
                char = s[j - 1]
                if pat == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif pat == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = char == pat and dp[i - 1][j - 1]

        return dp[m][n]


if __name__ == "__main__":
    s = "aa"
    p = "a"

    s = "aa"
    p = "*"

    s = "cb"
    p = "?a"

    s = "abcdefg"
    p = "ab*?g"

    s = "acdcb"
    p = "a*c?b"

    # s = ""
    # p = "*"

    # s = "abcabczzzde"
    # p = "*abc???de*"

    sol = SolutionBottomUp()
    print(sol.isMatch(s, p))
