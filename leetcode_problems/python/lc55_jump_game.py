class SolutionGreedyOne:
    def canJump(self, nums: list[int]) -> bool:
        p1 = 0
        p2 = 0
        n = len(nums)
        for i in range(n):
            p2 = max(p2, i + nums[i])
            if i == p1:
                if p1 == p2:
                    return len(nums) == 1 or p2 == n - 1
                p1 = p2
        return True


class SolutionGreedyTwo:
    def canJump(self, nums: list[int]) -> bool:
        max_reach = 0
        n = len(nums)
        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True


class SolutionDPBottomUp:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = [10**5] * n
        dp[0] = 0
        for i in range(n):
            for j in range(i + 1, min(i + 1 + nums[i], n)):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[n - 1] != 10**5


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    nums = [3, 2, 1, 0, 4]
    print(SolutionDPBottomUp().canJump(nums))
