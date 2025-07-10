MAX = 10**6


class SolutionRecursive:
    def editDistance(
        self,
        s1: str,
        s2: str,
    ) -> int:
        """
        s1 = "abc"
        s2 = "adc"

        На позиции i=1, j=1: s1[1]='b', s2[1]='d'
        Символы не совпадают, что делать?
        - Delete: удаляем 'b' из s1 -> сравниваем 'c' с 'd' (i+1, j)
        - Insert: вставляем 'd' в s1 -> сравниваем 'b' с 'c' (i, j+1)
        - Replace: заменяем 'b' на 'd' -> сравниваем 'c' с 'c' (i+1, j+1)
        """

        def rec(i: int, j: int) -> int:
            if i == m and j == n:
                return 0
            if i >= m:
                return n - j  # add string s2
            if j >= n:
                return m - i  # add string s1

            if s1[i] == s2[j]:
                return rec(i + 1, j + 1)
            else:
                return 1 + min(
                    rec(i + 1, j),  # delete
                    rec(i, j + 1),  # insert
                    rec(i + 1, j + 1),  # replace
                )

        m = len(s1)
        n = len(s2)
        return rec(0, 0)


class SolutionTopDown:
    def editDistance(
        self,
        s1: str,
        s2: str,
    ) -> int:
        def rec(i: int, j: int) -> int:
            if i == m and j == n:
                return 0
            if i >= m:
                return n - j
            if j >= n:
                return m - i

            key = (i, j)
            if key not in mem:
                if s1[i] == s2[j]:
                    mem[key] = rec(i + 1, j + 1)
                else:
                    mem[key] = 1 + min(
                        rec(i + 1, j),  # delete
                        rec(i, j + 1),  # insert
                        rec(i + 1, j + 1),  # replace
                    )
            return mem[key]

        m = len(s1)
        n = len(s2)
        mem = dict()
        return rec(0, 0)


class SolutionBottomUp:
    def editDistance(
        self,
        s1: str,
        s2: str,
    ) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # setup for full string edit on borders
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i][j - 1],  # insert
                        dp[i - 1][j],  # delete
                        dp[i - 1][j - 1],  # replace
                    )
        return dp[m][n]


class SolutionBottomUpOptimized:
    def editDistance(
        self,
        s1: str,
        s2: str,
    ) -> int:
        m = len(s1)
        n = len(s2)
        dp = [0] * (n + 1)
        ndp = [0] * (n + 1)

        # don't setup any borders
        # it's setuped as 0's
        # rest of values setuped dynamically by dp algorithm

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    ndp[j] = dp[j - 1]
                else:
                    ndp[j] = 1 + min(
                        ndp[j - 1],  # insert
                        dp[j],  # delete
                        dp[j - 1],  # replace
                    )
            dp, ndp = ndp, dp
        return dp[n]


if __name__ == "__main__":
    s1 = "geek"
    s2 = "gesek"

    s1 = "abcd"
    s2 = "bcfe"

    s1 = "GEEXSFRGEEKKS"
    s2 = "GEEKSFORGEEKS"

    print(SolutionRecursive().editDistance(s1, s2))
    print(SolutionTopDown().editDistance(s1, s2))
    print(SolutionBottomUp().editDistance(s1, s2))
    print(SolutionBottomUpOptimized().editDistance(s1, s2))
