class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        nums = sorted(nums)
        avgs = set()

        i = 0
        j = len(nums) - 1
        while i < j:
            min_num = nums[i]
            max_num = nums[j]

            avg = min_num + (max_num - min_num) / 2
            avgs.add(avg)

            i += 1
            j -= 1

        return len(avgs)


if __name__ == "__main__":
    nums = [4, 1, 4, 0, 3, 5, 7]
    print(Solution().distinctAverages(nums))
