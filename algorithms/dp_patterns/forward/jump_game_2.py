MAX = 10**7


class SolutionRecursive:
    def jump(self, nums: list[int]) -> int:
        def rec(i: int) -> int:
            if i >= n - 1:
                return 0

            mini = 10**7
            for j in range(1, nums[i] + 1):
                mini = min(mini, 1 + rec(i + j))
            return mini

        n = len(nums)
        return rec(0)


class SolutionTopDown:
    def jump(self, nums: list[int]) -> int:
        def rec(i: int) -> int:
            if i >= n - 1:
                return 0

            key = i
            if key not in mem:
                mem[key] = 10**7
                for j in range(1, nums[i] + 1):
                    mem[key] = min(mem[key], 1 + rec(i + j))
            return mem[key]

        n = len(nums)
        mem = {}
        return rec(0)


class SolutionBottomUp:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [MAX] * n
        dp[0] = 0
        for i in range(n):
            for j in range(1, nums[i] + 1):
                if i + j >= n:
                    continue
                dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[n - 1]


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    sol = SolutionBottomUp()
    print(sol.jump(nums))
