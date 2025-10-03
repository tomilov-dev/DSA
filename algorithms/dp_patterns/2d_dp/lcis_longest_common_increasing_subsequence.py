class Solution:
    def lcis(self, A: list[int], B: list[int]) -> int:
        n = len(A)
        m = len(B)
        dp = [0] * m
        for i in range(n):
            length = 0
            for j in range(m):
                if A[i] == B[j]:
                    dp[j] = max(dp[j], length + 1)
                if A[i] > B[j]:
                    length = max(length, dp[j])
        return max(dp)
