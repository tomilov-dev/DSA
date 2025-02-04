class Solution:
    def subsets(
        self,
        nums: list[int],
    ) -> list[list[int]]:
        def backtrack(i: int):
            res.append(stack[:])
            for j in range(i, len(nums)):
                stack.append(nums[j])
                backtrack(j + 1)
                stack.pop()

        res = []
        stack = []
        backtrack(0)
        return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
