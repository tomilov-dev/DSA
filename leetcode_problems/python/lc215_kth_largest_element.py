import random
from typing import List


class Solution:
    def reverse_partition(
        self,
        nums: List[int],
        start: int,
        end: int,
    ) -> int:
        x = nums[end]

        i = start - 1
        for j in range(start, end):
            if nums[j] >= x:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]

        i += 1
        nums[i], nums[end] = nums[end], nums[i]
        return i

    def random_reverse_partition(
        self,
        nums: List[int],
        start: int,
        end: int,
    ) -> int:
        i = random.choice(range(start, end + 1))
        nums[i], nums[end] = nums[end], nums[i]
        return self.reverse_partition(nums, start, end)

    def quickselect(
        self,
        nums: List[int],
        start: int,
        end: int,
        k: int,
    ) -> int:
        if start > end:
            return

        q = self.random_reverse_partition(nums, start, end)
        if q == k - 1:
            return nums[q]
        elif q > k - 1:
            return self.quickselect(nums, start, q - 1, k)
        else:
            return self.quickselect(nums, q + 1, end, k)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickselect(nums, 0, len(nums) - 1, k)


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    ans = 5

    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    ans = 4

    sol = Solution()
    print(sol.findKthLargest(nums, k))
