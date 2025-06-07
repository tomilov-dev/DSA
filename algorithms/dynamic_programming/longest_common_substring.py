MIN = -(10**6)


class SolutionRecursive:
    def longestCommonSubstr(
        self,
        s1: str,
        s2: str,
    ) -> int:
        def rec(i: int, j: int, c: int = 0) -> int:
            if i >= len(s1) or j >= len(s2):
                return c
            return max(
                rec(i + 1, j + 1, c + int(s1[i] == s2[j])),
                rec(i + 1, j, 0),
                rec(i, j + 1, 0),
            )

        return rec(0, 0)


class SolutionTopDownWithError:
    def longestCommonSubstr(
        self,
        s1: str,
        s2: str,
    ) -> int:
        """
        We can't optimize key more
        There is an error with this function
        """

        def rec(i: int, j: int, c: int = 0) -> int:
            if i >= len(s1) or j >= len(s2):
                return c

            key = (i, j, c)
            if key not in mem:
                if s1[i] == s2[j]:
                    mem[key] = rec(i + 1, j + 1, c + 1)
                else:
                    mem[key] = max(rec(i + 1, j, 0), rec(i, j + 1, 0))
            return mem[key]

        mem = {}
        return rec(0, 0)


class SolutionBottomUp:
    def longestCommonSubstr(
        self,
        s1: str,
        s2: str,
    ) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        maxi = MIN
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    maxi = max(maxi, dp[i][j])
        return maxi


class SolutionBottomUpOptimized:
    def longestCommonSubstr(
        self,
        s1: str,
        s2: str,
    ) -> int:
        m = len(s1)
        n = len(s2)

        dp = [0] * (n + 1)
        maxi = MIN
        for i in range(1, m + 1):
            ndp = [0] * (n + 1)
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    ndp[j] = 1 + dp[j - 1]
                    maxi = max(maxi, ndp[j])
            dp = ndp
        return maxi


if __name__ == "__main__":
    s1 = "ABCDGH"
    s2 = "ACDGHR"

    s1 = "adac"
    s2 = "adadac"

    s1 = "LRBBMQBHCDARZOWKKYHIDDQSCDXRJMOWFRXSJYBLDBEFSARCBYNECDYGGXXPKLORELLNMPAPQFWKHOPKMCO"
    s2 = "QHNWNKUEWHSQMGBBUQCLJJIVSWMDKQTBXIXMVTRRBLJPTNSNFWZQFJMAFADRRWSOFSBCNUVQHFFBSAQXWPQCAC"
    # print(SolutionRecursive().longestCommonSubstr(s1, s2))
    print(SolutionTopDownWithError().longestCommonSubstr(s1, s2))
    print(SolutionBottomUp().longestCommonSubstr(s1, s2))
    print(SolutionBottomUpOptimized().longestCommonSubstr(s1, s2))
