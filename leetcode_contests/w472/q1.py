class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        mem = dict()
        for num in nums:
            mem[num] = True

        miss = k
        while miss < 1000:
            if miss not in mem:
                return miss
            miss += k
        return -1


if __name__ == "__main__":
    nums = [8, 2, 3, 4, 6]
    k = 2
    sol = Solution()
    print(sol.missingMultiple(nums, k))
