class Solution:
    def alternatingSum(self, nums: list[int]) -> int:
        sm = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                sm += num
            else:
                sm -= num
        return sm


if __name__ == "__main__":
    nums = [1, 3, 5, 7]
    print(Solution().alternatingSum(nums))
