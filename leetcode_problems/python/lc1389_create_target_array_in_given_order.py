class Solution:
    def createTargetArray(
        self,
        nums: list[int],
        index: list[int],
    ) -> list[int]:
        res = []
        for i in range(len(nums)):
            res.insert(index[i], nums[i])
        return res


if __name__ == "__main__":
    nums = [0, 1, 2, 3, 4]
    index = [0, 1, 2, 2, 1]

    nums = [1, 2, 3, 4, 0]
    index = [0, 1, 2, 3, 0]

    nums = [4, 2, 4, 3, 2]
    index = [0, 0, 1, 3, 1]
    print(Solution().createTargetArray(nums, index))
