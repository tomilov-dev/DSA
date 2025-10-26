class Solution:
    def numGoodSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        pref = [0]
        for num in nums:
            pref.append(pref[-1] + num)

        good = set()
        for i in range(n):
            for j in range(i + 1, n + 1):
                if (pref[j] - pref[i]) % k == 0:
                    good.add(tuple(nums[i:j]))
        return len(good)


if __name__ == "__main__":
    nums = [1, 2, 3]
    k = 3

    nums = [2, 2, 2, 2, 2, 2]
    k = 6

    sol = Solution()
    print(sol.numGoodSubarrays(nums, k))
