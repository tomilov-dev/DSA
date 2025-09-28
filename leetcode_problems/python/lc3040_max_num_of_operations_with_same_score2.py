class SolutionRecursive:
    def maxOperations(self, nums: list[int]) -> int:
        def rec(i: int, j: int, score: int | None) -> int:
            if i >= j:
                return 0

            sub = 0
            if i + 1 <= j:
                first = nums[i] + nums[i + 1]
                if score is None or first == score:
                    sub = max(sub, 1 + rec(i + 2, j, first))

            if j - 1 >= i:
                last = nums[j] + nums[j - 1]
                if score is None or last == score:
                    sub = max(sub, 1 + rec(i, j - 2, last))

            if i < j:
                both = nums[i] + nums[j]
                if score is None or both == score:
                    sub = max(sub, 1 + rec(i + 1, j - 1, both))
            return sub

        n = len(nums)
        return rec(0, n - 1, None)


class SolutionTopDown:
    def maxOperations(self, nums: list[int]) -> int:
        def rec(i: int, j: int, score: int | None) -> int:
            if i >= j:
                return 0

            key = (i, j, score)
            if key not in mem:
                sub = 0
                if i + 1 <= j:
                    first = nums[i] + nums[i + 1]
                    if score is None or first == score:
                        sub = max(sub, 1 + rec(i + 2, j, first))

                if j - 1 >= i:
                    last = nums[j] + nums[j - 1]
                    if score is None or last == score:
                        sub = max(sub, 1 + rec(i, j - 2, last))

                if i < j:
                    both = nums[i] + nums[j]
                    if score is None or both == score:
                        sub = max(sub, 1 + rec(i + 1, j - 1, both))
                mem[key] = sub
            return mem[key]

        n = len(nums)
        mem = {}
        return rec(0, n - 1, None)


class SolutionBottomUp:
    def maxOperations(self, nums: list[int]) -> int:
        n = len(nums)
        initial_scores = [
            nums[0] + nums[1],
            nums[0] + nums[n - 1],
            nums[n - 2] + nums[n - 1],
        ]
        res = 0
        for iscore in initial_scores:
            dp = [[0] * (n + 1) for _ in range(n + 1)]
            for i in range(2, n + 1):
                for l in range(0, n - i + 1):
                    r = l + i - 1
                    # first two
                    if nums[l] + nums[l + 1] == iscore:
                        dp[i][l] = max(dp[i][l], 1 + dp[i - 2][l + 2])
                    # both ends
                    if nums[l] + nums[r] == iscore:
                        dp[i][l] = max(dp[i][l], 1 + dp[i - 2][l + 1])
                    # last two
                    if nums[r - 1] + nums[r] == iscore:
                        dp[i][l] = max(dp[i][l], 1 + dp[i - 2][l])
            res = max(res, dp[n][0])
        return res


if __name__ == "__main__":
    nums = [3, 2, 1, 2, 3, 4]
    print(SolutionBottomUp().maxOperations(nums))
