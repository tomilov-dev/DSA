class Solution:
    def minMaxGame(self, nums: list[int], op=lambda x: min(x)) -> int:
        if len(nums) == 1:
            return nums[0]

        mid = len(nums) // 2
        l = self.minMaxGame(nums[:mid], lambda x: min(x))
        r = self.minMaxGame(nums[mid:], lambda x: max(x))
        return op([l, r])


class Solution2:
    def minMaxGame(self, nums: list[int]) -> int:
        while len(nums) > 1:
            new_nums = []
            for i in range(len(nums) // 2):
                if i % 2 == 0:
                    new_nums.append(min(nums[2 * i], nums[2 * i + 1]))
                else:
                    new_nums.append(max(nums[2 * i], nums[2 * i + 1]))
            nums = new_nums
        return nums[0]


if __name__ == "__main__":
    nums = [1, 3, 5, 2, 4, 8, 2, 2]
    nums = [93, 40]
    print(Solution().minMaxGame(nums))
