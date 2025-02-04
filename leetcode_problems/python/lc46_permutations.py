class Solution:
    def permute(
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

                used[j] = True
                stack.append(nums[j])
                backtrack()
                stack.pop()
                used[j] = False

        res = []
        stack = []
        used = [False] * len(nums)
        backtrack()
        return res


class Solution2:
    def permute(
        self,
        nums: list[int],
    ) -> list[list[int]]:
        def backtrack(start: int) -> None:
            if start == len(nums):
                res.append(nums[:])
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        res = []
        backtrack(0)
        return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution2().permute(nums))
