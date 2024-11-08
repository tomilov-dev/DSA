class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        finder = nums[0]
        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]

        return finder


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    print(Solution().findDuplicate(nums))
