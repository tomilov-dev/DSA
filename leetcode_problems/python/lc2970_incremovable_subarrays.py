class Solution:
    def incremovableSubarrayCount(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        count = 1
        left = 0
        while left < n - 1 and nums[left] < nums[left + 1]:
            left += 1
        count += left + 1

        right = n - 1
        while right > 0 and nums[right - 1] < nums[right]:
            right -= 1
        count += n - right

        if left >= right:
            return (n * (n + 1)) // 2

        left = 0
        while left < right and right < n:
            if nums[left] < nums[right]:
                count += 1 if right == n - 1 else (n - right)
                if left < n - 1 and nums[left] < nums[left + 1]:
                    left += 1
                else:
                    break
            else:
                right += 1

        return count


if __name__ == "__main__":
    nums = [6, 5, 7, 8]
    print(Solution().incremovableSubarrayCount(nums))
