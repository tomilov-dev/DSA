class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        snums = sorted(nums)

        i = 0
        sum = 0
        while i < len(snums):
            if i % 2 == 0:
                sum += snums[i]
            else:
                pass

            i += 1

        return sum


if __name__ == "__main__":
    nums = [6, 2, 6, 5, 1, 2]
    print(Solution().arrayPairSum(nums))
