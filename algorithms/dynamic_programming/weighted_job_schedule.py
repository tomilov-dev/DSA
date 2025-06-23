class SolutionRecursive:
    def count(
        self,
        jobs: list[list[int]],
    ) -> int:
        def rec(i: int, j: int) -> int:
            if i >= n:
                return 0

            take = 0
            if j == -1 or jobs[j][1] <= jobs[i][0]:
                take = jobs[i][2] + rec(i + 1, i)
            not_take = rec(i + 1, j)
            return max(take, not_take)

        jobs.sort()
        n = len(jobs)
        return rec(0, -1)


class SolutionTopDown:
    def count(
        self,
        jobs: list[list[int]],
    ) -> int:
        def rec(i: int, j: int) -> int:
            if i >= n:
                return 0

            key = (i, j)
            if key not in mem:
                take = 0
                if j == -1 or jobs[j][1] <= jobs[i][0]:
                    take = jobs[i][2] + rec(i + 1, i)
                not_take = rec(i + 1, j)
                mem[key] = max(take, not_take)
            return mem[key]

        jobs.sort()
        n = len(jobs)
        mem = {}
        return rec(0, -1)


class SolutionBottomUp:
    def count(
        self,
        jobs: list[list[int]],
    ) -> int:
        jobs.sort()
        n = len(jobs)
        dp = [j[2] for j in jobs]
        for i in range(1, n):
            for j in range(i):
                if jobs[j][1] <= jobs[i][0]:
                    dp[i] = max(dp[i], dp[j] + jobs[i][2])
        return max(dp)


if __name__ == "__main__":
    jobs = [
        [1, 2, 50],
        [3, 5, 20],
        [6, 19, 100],
        [2, 100, 200],
    ]

    print(SolutionRecursive().count(jobs))
    print(SolutionTopDown().count(jobs))
    print(SolutionBottomUp().count(jobs))
