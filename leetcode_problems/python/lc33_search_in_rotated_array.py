class Solution:
    def find_offset(self, nums: list[int]) -> int:
        def is_good(
            array: list[int],
            index: int,
        ) -> bool:
            return array[index] > array[-1]

        low, high = -1, len(nums) - 1
        while high - low > 1:
            mid = low + (high - low) // 2
            if is_good(nums, mid):
                low = mid
            else:
                high = mid
        return high

    def search(
        self,
        nums: list[int],
        target: int,
    ) -> int:
        def is_good(
            nums: list[int],
            index: int,
            offset: int,
            target: int,
        ) -> bool:
            index = (index + offset) % len(nums)
            return nums[index] <= target

        offset = self.find_offset(nums)
        low, high = 0, len(nums)
        while high - low > 1:
            mid = low + (high - low) // 2
            if is_good(nums, mid, offset, target):
                low = mid
            else:
                high = mid

        res = (low + offset) % len(nums)
        return res if nums[res] == target else -1


class Solution2:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] >= nums[low]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(Solution().search(nums, target))
