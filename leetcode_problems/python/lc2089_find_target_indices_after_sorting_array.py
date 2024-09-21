class Solution:
    def bsearch(
        self,
        array: list[int],
        target: int,
    ) -> int | None:
        bot = 0
        top = len(array) - 1
        while bot <= top:
            mid = bot + (top - bot) // 2
            if array[mid] == target:
                return mid
            elif array[mid] < target:
                bot = mid + 1
            else:
                top = mid - 1

        return None

    def targetIndices(
        self,
        nums: list[int],
        target: int,
    ) -> list[int]:
        nums.sort()
        index = self.bsearch(nums, target)
        if index is None:
            return []

        min_index = index
        max_index = index
        while min_index - 1 >= 0 and nums[min_index - 1] == target:
            min_index -= 1

        while max_index + 1 < len(nums) and nums[max_index + 1] == target:
            max_index += 1

        if min_index == max_index:
            return [min_index]
        return list(range(min_index, max_index + 1))


class Solution2:
    def findFirst(self, array: list[int], target: int) -> int:
        bot = 0
        top = len(array) - 1
        while bot <= top:
            mid = bot + (top - bot) // 2
            if array[mid] < target:
                bot = mid + 1
            else:
                top = mid - 1
        return bot

    def findLast(self, array: list[int], target: int) -> int:
        bot = 0
        top = len(array) - 1
        while bot <= top:
            mid = bot + (top - bot) // 2
            if array[mid] <= target:
                bot = mid + 1
            else:
                top = mid - 1
        return top

    def targetIndices(
        self,
        nums: list[int],
        target: int,
    ) -> list[int]:
        nums.sort()
        first = self.findFirst(nums, target)
        last = self.findLast(nums, target)

        if first <= last and first < len(nums) and nums[first] == target:
            return list(range(first, last + 1))
        return []


if __name__ == "__main__":
    nums = [1, 2, 5, 2, 3]
    target = 2

    # print(Solution().targetIndices(nums, target))
    print(Solution2().targetIndices(nums, target))
