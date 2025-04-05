class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        def backtrack(i: int) -> bool:
            if i >= n:
                return all(s == t for s in subs)

            for isub in range(k):
                if subs[isub] + nums[i] <= t:
                    subs[isub] += nums[i]
                    if backtrack(i + 1):
                        return True
                    subs[isub] -= nums[i]

                if subs[isub] == 0:
                    break

            return False

        n = len(nums)
        nsum = sum(nums)
        if nsum <= 0 or nsum % k != 0:
            return False

        t = nsum // k
        if max(nums) > t:
            return False

        nums.sort(reverse=True)
        subs = [0] * k
        return backtrack(0)


if __name__ == "__main__":
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4

    nums = [1, 2, 3, 4]
    k = 3
    print(Solution().canPartitionKSubsets(nums, k))
