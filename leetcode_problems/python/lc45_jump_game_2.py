class SolutionGreedy:
    def jump(self, nums: list[int]) -> int:
        p1 = 0
        p2 = 0
        n = len(nums)
        c = 0
        for i in range(n - 1):
            p2 = max(p2, i + nums[i])
            if i == p1:
                c += 1
                p1 = p2
        return c


class SolutionDPBottomUp:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [10**4] * n
        dp[0] = 0
        for i in range(n - 1):
            for j in range(i + 1, min(i + 1 + nums[i], n)):
                dp[j] = min(dp[j], dp[i] + 1)
        return dp[n - 1]


class SolutionDPTopDown:
    def jump(self, nums: list[int]) -> int:
        def dp(i: int) -> int:
            if mem[i] != -1:
                return mem[i]

            mem[i] = 10**4
            for j in range(i):
                if j + nums[j] >= i:
                    mem[i] = min(mem[i], dp(j) + 1)

            return mem[i]

        n = len(nums)
        mem = [-1] * n
        mem[0] = 0
        return dp(n - 1)


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    # print(SolutionGreedy().jump(nums))
    # print(SolutionDPBottomUp().jump(nums))
    print(SolutionDPTopDown().jump(nums))
