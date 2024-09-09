class Solution:
    def kLengthApart(
        self,
        nums: list[int],
        k: int,
    ) -> bool:
        index = 0
        while index < len(nums) and nums[index] == 0:
            index += 1

        dist = 0
        for i in range(index, len(nums)):
            if nums[i] == 0:
                dist += 1

            else:
                if dist < k:
                    return False
                dist = 0

        return True


if __name__ == "__main__":
    nums = [1, 0, 0, 0, 1, 0, 0, 1]
    k = 2

    nums = [1, 0, 0, 1, 0, 1]
    k = 2

    nums = [1, 1, 1, 0]
    k = 3

    print(Solution().kLengthApart(nums, k))
