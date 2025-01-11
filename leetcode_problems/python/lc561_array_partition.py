class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        shift = 10**4 + 1
        count = [0] * (10**4 + 1) * 2
        for num in nums:
            count[shift + num] += 1

        snums = []
        for num, fq in enumerate(count):
            if not fq:
                continue
            snums.extend([num - shift] * fq)

        i = 0
        sum = 0
        while i < len(snums):
            if i % 2 == 0:
                sum += snums[i]
            i += 1

        return sum


class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        nums.sort()
        return sum(nums[i] for i in range(0, len(nums), 2))


if __name__ == "__main__":
    nums = [6, 2, 6, 5, 1, 2]
    print(Solution().arrayPairSum(nums))
