class SolutionBacktracking:
    def maxProduct(
        self,
        nums: list[int],
    ) -> int:
        def backtrack(i: int):
            nonlocal cur
            nonlocal maxi

            if i >= len(nums):
                return None

            cur *= nums[i]
            maxi = max(maxi, cur)
            backtrack(i + 1)
            cur /= nums[i]

        maxi = min(nums)
        cur = 1
        backtrack(0)
        return maxi


class SolutionIter:
    def maxProduct(
        self,
        nums: list[int],
    ) -> int:
        n = len(nums)
        maxi = min(nums)
        for i in range(n):
            sub = 1
            for j in range(i, n):
                sub *= nums[j]
                maxi = max(maxi, sub)

        return maxi


class SolutionDPBottomUp:
    def maxProduct(
        self,
        nums: list[int],
    ) -> int:
        n = len(nums)
        max_dp = [0] * n
        min_dp = [0] * n

        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        for i in range(1, n):
            if nums[i] >= 0:
                max_dp[i] = max(nums[i], max_dp[i - 1] * nums[i])
                min_dp[i] = min(nums[i], min_dp[i - 1] * nums[i])
            else:
                max_dp[i] = max(nums[i], min_dp[i - 1] * nums[i])
                min_dp[i] = min(nums[i], max_dp[i - 1] * nums[i])

        return max(max_dp)


class SolutionDPBottomUpOptimized:
    def maxProduct(
        self,
        nums: list[int],
    ) -> int:
        n = len(nums)
        if n == 0:
            return 0

        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for i in range(1, n):
            if nums[i] < 0:
                max_product, min_product = min_product, max_product

            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])
            result = max(result, max_product)

        return result


if __name__ == "__main__":
    nums = [2, 3, -2, 4]
    print(SolutionDPBottomUp().maxProduct(nums))
