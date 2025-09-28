class Solution:
    def maxOperations(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        prev: int | None = None
        for i in range(n // 2):
            cur = nums[i * 2] + nums[i * 2 + 1]
            if prev is None or cur == prev:
                total += 1
                prev = cur
            else:
                break
        return total


if __name__ == "__main__":
    nums = [3, 2, 1, 4, 5]
    print(Solution().maxOperations(nums))
