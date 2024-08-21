from typing import Callable


class Solution:
    def bsearch(
        self,
        nums: list[int],
        bot: int,
        top: int,
        find_positive: bool,
    ) -> int | None:
        index = None
        while bot <= top:
            mid = bot + (top - bot) // 2
            if find_positive:
                if nums[mid] > 0:
                    index = mid
                    top = mid - 1
                else:
                    bot = mid + 1

            else:
                if nums[mid] < 0:
                    index = mid
                    bot = mid + 1
                else:
                    top = mid - 1

        return index

    def maximumCount(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return int(nums[0] != 0)

        neg_index = self.bsearch(nums, 0, len(nums) - 1, find_positive=False)
        pos_index = self.bsearch(nums, 0, len(nums) - 1, find_positive=True)

        negatives = neg_index + 1 if neg_index is not None else 0
        positives = len(nums) - pos_index if pos_index is not None else 0

        return max(negatives, positives)


if __name__ == "__main__":
    nums = [-2, -2, -1]
    print(Solution().maximumCount(nums))
