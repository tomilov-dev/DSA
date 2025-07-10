class SolutionRecursive:
    def count(self, s: str) -> int:
        def is_palindrome(i: int, j: int) -> bool:
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if is_palindrome(i, j):
                    res += 1
        return res


class SolutionTopDown:
    def count(self, s: str) -> int:
        def is_palindrome(i: int, j: int) -> bool:
            if i == j:
                return True
            if abs(i - j) == 1:
                return s[i] == s[j]

            key = (i, j)
            if key not in mem:
                mem[key] = s[i] == s[j] and is_palindrome(i + 1, j - 1)
            return mem[key]

        n = len(s)
        res = 0
        mem = dict()
        for i in range(n):
            for j in range(i + 1, n):
                if is_palindrome(i, j):
                    res += 1
        return res


class SolutionBottomUp:
    def count(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = True

        res = 0
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                res += 1

        # Handle palindromes of length
        # greater than 2 (gap >= 2)
        for gap in range(2, n):
            for i in range(n - gap):
                j = i + gap
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    res += 1

        return res


if __name__ == "__main__":
    s = "abaab"
    print(SolutionRecursive().count(s))
    print(SolutionTopDown().count(s))
    print(SolutionBottomUp().count(s))
