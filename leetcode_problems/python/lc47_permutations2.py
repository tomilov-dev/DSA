class Solution:
    def permuteUnique(
        self,
        nums: list[int],
    ) -> list[list[int]]:
        def backtrack() -> None:
            if len(stack) == len(nums):
                res.append(stack[:])
                return None

            for j in range(len(nums)):
                if used[j]:
                    continue
                if j > 0 and nums[j] == nums[j - 1] and not used[j - 1]:
                    continue

                used[j] = True
                stack.append(nums[j])
                backtrack()
                stack.pop()
                used[j] = False

        nums.sort()
        res = []
        stack = []
        used = [False] * len(nums)
        backtrack()
        return res


if __name__ == "__main__":
    nums = [1, 1, 2]
    print(Solution().permuteUnique(nums))
