MIN = -(10**7)


class SolutionRecursive:
    def maxSubArray(self, nums: list[int]) -> int:
        def rec(i, cur):
            if i >= n:
                return cur
            return max(cur + nums[i], rec(i + 1, cur + nums[i]))

        n = len(nums)
        return max(rec(i, 0) for i in range(n))


class SolutionTopDown:
    def maxSubArray(self, nums: list[int]) -> int:
        def rec(i: int):
            if i >= n:
                return MIN
            if i not in mem:
                mem[i] = max(nums[i], rec(i + 1) + nums[i])
            return mem[i]

        n = len(nums)
        mem = {}
        return max(rec(i) for i in range(n))


class SolutionBottomUp:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        dp = nums[:]
        for i in range(1, n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    sol = SolutionBottomUp()
    print(sol.maxSubArray(nums))
