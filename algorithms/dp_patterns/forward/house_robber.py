class SolutionRecursive:
    def rob(self, nums: list[int]) -> int:
        def rec(i: int) -> int:
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            return max(
                nums[i] + rec(i - 2),
                rec(i - 1),
            )

        n = len(nums)
        if n == 1:
            return nums[0]

        return rec(n - 1)


class SolutionTopDown:
    def rob(self, nums: list[int]) -> int:
        def rec(i: int) -> int:
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i not in mem:
                mem[i] = max(
                    nums[i] + rec(i - 2),
                    rec(i - 1),
                )
            return mem[i]

        n = len(nums)
        if n == 1:
            return nums[0]

        mem = {}
        return rec(n - 1)


class SolutionBottomUp:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        for i in range(2, n + 1):
            dp[i] = max(nums[i - 1] + dp[i - 2], dp[i - 1])
        return dp[n]


class SolutionMemoryOptimized:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        n1 = 0
        n2 = nums[0]
        for i in range(2, n + 1):
            n3 = max(nums[i - 1] + n1, n2)
            n1 = n2
            n2 = n3
        return n2


if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    sol = SolutionMemoryOptimized()
    res = sol.rob(nums)
    print(res)
