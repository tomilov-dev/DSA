class Solution:
    def bfirts(
        self,
        nums: list[int],
        target: int,
    ) -> int:
        def is_good(val: int, target: int) -> bool:
            return val < target

        low, high = -1, len(nums) - 1
        while high - low > 1:
            mid = low + (high - low) // 2
            if is_good(nums[mid], target):
                low = mid
            else:
                high = mid

        if high >= 0 and nums[high] == target:
            return high
        return -1

    def blast(
        self,
        nums: list[int],
        target: int,
    ) -> int:
        def is_good(val: int, target: int) -> bool:
            return val <= target

        low, high = 0, len(nums)
        while high - low > 1:
            mid = low + (high - low) // 2
            if is_good(nums[mid], target):
                low = mid
            else:
                high = mid

        if low >= 0 and nums[low] == target:
            return low
        return -1

    def searchRange(
        self,
        nums: list[int],
        target: int,
    ) -> list[int]:
        i = self.bfirts(nums, target)
        if i > -1:
            return [i, self.blast(nums, target)]
        return [-1, -1]


class Solution2:
    def bfirts(
        self,
        nums: list[int],
        target: int,
    ) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        if low < len(nums) and nums[low] == target:
            return low
        return -1

    def blast(
        self,
        nums: list[int],
        target: int,
    ) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1

        if high >= 0 and nums[high] == target:
            return high
        return -1

    def searchRange(
        self,
        nums: list[int],
        target: int,
    ) -> list[int]:
        i = self.bfirts(nums, target)
        if i > -1:
            return [i, self.blast(nums, target)]
        return [-1, -1]


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 8, 8, 10]
    target = 8
    print(Solution2().searchRange(nums, target))
