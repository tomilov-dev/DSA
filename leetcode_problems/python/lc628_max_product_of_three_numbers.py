import random


class Solution:
    def max_prod(self, nums: list[int]) -> int:
        sums = [
            nums[0] * nums[1] * nums[2],
            nums[0] * nums[1] * nums[-1],
            nums[-1] * nums[-2] * nums[-3],
        ]
        return max(sums)

    def maximumProduct(
        self,
        nums: list[int],
    ) -> int:
        shift = 1001
        count = [0 for _ in range(1001 * 2)]
        for num in nums:
            count[num + shift] += 1
        index = 0
        for num, c in enumerate(count):
            for _ in range(c):
                nums[index] = num - shift
                index += 1

        return self.max_prod(nums)


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    random.shuffle(nums)
    print(Solution().maximumProduct(nums))
