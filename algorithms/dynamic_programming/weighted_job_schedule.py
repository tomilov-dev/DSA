class Solution:
    def count(
        self,
        jobs: list[list[int]],
    ) -> int:
        jobs.sort()
        n = len(jobs)
        dp = [0] * n
        for i in range(n):
            dp[i] = jobs[i][2]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if jobs[i][1] > jobs[j][0]:
                    continue
                dp[i] = max(dp[i], dp[j] + jobs[i][2])
        return dp[0]


if __name__ == "__main__":
    jobs = [
        [1, 2, 50],
        [3, 5, 20],
        [6, 19, 100],
        [2, 100, 200],
    ]
    print(Solution().count(jobs))
