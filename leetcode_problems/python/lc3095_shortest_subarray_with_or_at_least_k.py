class Solution:
    def minimumSubarrayLength(
        self,
        nums: list[int],
        k: int,
    ) -> int:
        mini = 100
        for p1 in range(len(nums)):
            cur = nums[p1]
            p2 = p1 + 1
            while p2 < len(nums) and cur < k:
                cur |= nums[p2]
                p2 += 1

            if cur >= k:
                mini = min(mini, p2 - p1)

        return mini if mini < 100 else -1


if __name__ == "__main__":
    nums = [1, 2, 3]
    k = 2
    print(Solution().minimumSubarrayLength(nums, k))
