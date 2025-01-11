class Solution:
    def numSubarrayProductLessThanK(
        self,
        nums: list[int],
        k: int,
    ) -> int:
        if k <= 1:
            return 0

        prod = 1
        count = 0
        left = 0

        for right in range(len(nums)):
            prod *= nums[right]
            while prod >= k and left <= right:
                prod //= nums[left]
                left += 1
            count += right - left + 1

        return count


if __name__ == "__main__":
    nums = [10, 5, 2, 6]
    k = 100
    print(Solution().numSubarrayProductLessThanK(nums, k))
