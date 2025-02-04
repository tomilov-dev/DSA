class Solution:
    def subsetXORSum(
        self,
        nums: list[int],
    ) -> int:
        def backtrack(i: int):
            nonlocal xor
            nonlocal res

            res += xor
            for j in range(i, len(nums)):
                xor ^= nums[j]
                backtrack(j + 1)
                xor ^= nums[j]

        res = 0
        xor = 0
        backtrack(0)
        return res


if __name__ == "__main__":
    nums = [5, 1, 6]
    print(Solution().subsetXORSum(nums))
