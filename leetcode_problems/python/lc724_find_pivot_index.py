class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        prefix = self.build_prefix(nums)
        for i in range(0, len(nums)):
            sum1 = self.find_sum(prefix, 0, i)
            sum2 = self.find_sum(prefix, i, len(nums) - 1)
            if sum1 == sum2:
                return i
        return -1

    def build_prefix(self, nums: list[int]) -> list[int]:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        return prefix

    def find_sum(
        self,
        prefix: list[int],
        l: int,
        r: int,
    ) -> int:
        return prefix[r + 1] - prefix[l]


class Solution2:
    def pivotIndex(self, nums: list[int]) -> int:
        all_sum = sum(nums)
        cur_sum = 0
        for i in range(len(nums)):
            if all_sum - nums[i] - cur_sum == cur_sum:
                return i
        return -1


if __name__ == "__main__":
    nums = [2, 1, -1]
    print(Solution2().pivotIndex(nums))
