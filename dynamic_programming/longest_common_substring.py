from pprint import pprint


class SolutionBottomUp:
    def longestCommonSubstr(
        self,
        s1: str,
        s2: str,
    ) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        maxi = 0
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

        maxi = 0
        for i in range(1, m + 1):
            new_dp = [0] * (n + 1)
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    new_dp[j] = dp[j - 1] + 1
                    maxi = max(maxi, new_dp[j])
            dp = new_dp
        return maxi


if __name__ == "__main__":
    s1 = "ABCDGH"
    s2 = "ACDGHR"

    s1 = "adac"
    s2 = "adadac"

    # s1 = "LRBBMQBHCDARZOWKKYHIDDQSCDXRJMOWFRXSJYBLDBEFSARCBYNECDYGGXXPKLORELLNMPAPQFWKHOPKMCO"
    # s2 = "QHNWNKUEWHSQMGBBUQCLJJIVSWMDKQTBXIXMVTRRBLJPTNSNFWZQFJMAFADRRWSOFSBCNUVQHFFBSAQXWPQCAC"
    print(SolutionBottomUp().longestCommonSubstr(s1, s2))
    print(SolutionBottomUpOptimized().longestCommonSubstr(s1, s2))
