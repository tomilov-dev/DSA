class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        px = {0: 1}
        count = 0

        curr_px = 0
        for index, num in enumerate(nums):
            curr_px += num
            count += px.get(curr_px - k, 0)
            px[curr_px] = px.get(curr_px, 0) + 1

        return count


if __name__ == "__main__":
    nums = [1, 2, 3]
    k = 3
    print(Solution().subarraySum(nums, k))
