class Solution:
    def subsetsWithDup(
        self,
        nums: list[int],
    ) -> list[list[int]]:
        def backtrack(i: int):
            res.append(stack[:])
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue

                stack.append(nums[j])
                backtrack(j + 1)
                stack.pop()

        nums.sort()
        res = []
        stack = []
        backtrack(0)
        return res


if __name__ == "__main__":
    nums = [1, 2, 2]
    nums = [4, 4, 4, 1, 4]
    print(Solution().subsetsWithDup(nums))
