class Solution:
    def maxDigit(self, num: int) -> int:
        max_digit = 0
        for digit in str(num):
            max_digit = max(max_digit, int(digit))
        return max_digit

    def maxSum(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return -1

        res = -1
        max_num = [0 for _ in range(10)]
        for num in nums:
            max_d = self.maxDigit(num)
            if max_num[max_d]:
                res = max(res, max_num[max_d] + num)
            max_num[max_d] = max(max_num[max_d], num)

        return res


if __name__ == "__main__":
    nums = [2536, 1313, 3366, 162]
    nums = [84, 91, 18, 59, 27, 9, 81, 33, 17, 58]
    print(Solution().maxSum(nums))
