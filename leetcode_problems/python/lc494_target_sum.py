class Solution:
    def findTargetSumWays(
        self,
        nums: list[int],
        target: int,
    ) -> int:
        def backtrack(
            i: int = 0,
        ) -> None:
            nonlocal count
            nonlocal target
            nonlocal whsum
            if i == len(nums):
                if target == 0:
                    count += 1
                return None
            if abs(target) > abs(whsum):
                return None

            var = [-nums[i], nums[i]]
            for num in var:
                target -= num
                whsum -= abs(num)
                backtrack(i + 1)
                whsum += abs(num)
                target += num

        count = 0
        whsum = sum(nums)
        backtrack(0)
        return count


class SolutionMemoization:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        def backtrack(i: int, current_sum: int) -> int:
            if i == len(nums):
                return 1 if current_sum == target else 0
            if (i, current_sum) in memo:
                return memo[(i, current_sum)]

            add = backtrack(i + 1, current_sum + nums[i])
            subtract = backtrack(i + 1, current_sum - nums[i])

            memo[(i, current_sum)] = add + subtract
            return memo[(i, current_sum)]

        memo = {}
        return backtrack(0, 0)


class SolutionDP:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total_sum = sum(nums)
        if abs(target) > total_sum:
            return 0
        if (total_sum + target) % 2 != 0:
            return 0

        subset_sum = (total_sum + target) // 2
        dp = [0] * (subset_sum + 1)
        dp[0] = 1

        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]

        return dp[subset_sum]


if __name__ == "__main__":
    nums = [1, 1, 1, 1, 1]
    target = 3
    print(Solution().findTargetSumWays(nums, target))
