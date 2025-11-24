class SolutionTLE:
    def maxBalancedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        maxi = 0
        for i in range(n):
            xor = 0
            even = 0
            odd = 0
            for j in range(i, n):
                num = nums[j]
                xor ^= num
                if num % 2 == 0:
                    even += 1
                else:
                    odd += 1
                if xor == 0 and even == odd:
                    maxi = max(maxi, j - i + 1)
        return maxi


class Solution:
    def maxBalancedSubarray(self, nums: list[int]) -> int:
        xor = 0
        even = 0
        odd = 0
        prev = {}
        prev[(0, 0)] = -1
        maxi = 0
        for i, num in enumerate(nums):
            xor ^= num
            if num % 2 == 0:
                even += 1
            else:
                odd += 1
            pkey = (xor, even - odd)
            if pkey in prev:
                maxi = max(maxi, i - prev[pkey])
            else:
                prev[pkey] = i
        return maxi


if __name__ == "__main__":
    nums = [3, 1, 3, 2, 0]
    nums = [3, 2, 8, 5, 4, 14, 9, 15]
    # nums = [0]
    print(Solution().maxBalancedSubarray(nums))
