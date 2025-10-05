class SolutionTopDown:
    def longestSubsequence(self, nums: list[int]) -> int:
        def rec(i: int, xor: int) -> int:
            if i >= n:
                return int(xor != 0)

            key = (i, xor)
            if key not in mem:
                take = 1 + rec(i + 1, xor ^ nums[i])
                not_take = rec(i + 1, nums[i])
                mem[key] = max(take, not_take)
            return mem[key]

        n = len(nums)
        mem = {}
        return rec(1, nums[0])


if __name__ == "__main__":
    nums = [1, 2, 3]
    nums = [7, 6, 1, 9]
    nums = [1, 6, 6]
    print(SolutionTopDown().longestSubsequence(nums))
