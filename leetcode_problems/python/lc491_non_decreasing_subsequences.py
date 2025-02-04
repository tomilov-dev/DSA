class Solution:
    def findSubsequences(
        self,
        nums: list[int],
    ) -> list[list[int]]:
        def backtrack(i: int) -> None:
            if len(stack) >= 2:
                res.append(stack[:])

            used = set()
            for j in range(i, len(nums)):
                if nums[j] in used:
                    continue
                if stack and stack[-1] > nums[j]:
                    continue

                used.add(nums[j])
                stack.append(nums[j])

                backtrack(j + 1)
                stack.pop()

        res = []
        stack = []
        backtrack(0)
        return res


if __name__ == "__main__":
    nums = [4, 6, 7, 7]
    print(Solution().findSubsequences(nums))
