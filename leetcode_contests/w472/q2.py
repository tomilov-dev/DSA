class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        longest = 0
        n = len(nums)
        for i in range(0, n):
            odd = 0
            even = 0
            mem: dict[int, bool] = dict()
            for j in range(i, n):
                num = nums[j]
                if num not in mem:
                    if num % 2 == 0:
                        odd += 1
                    else:
                        even += 1

                mem[num] = True
                cur = j - i + 1
                if odd == even:
                    longest = max(longest, cur)
        return longest


if __name__ == "__main__":
    nums = [2, 5, 4, 3]
    # nums = [1, 2, 3, 2]
    # nums = [3, 2, 2, 5, 4]
    sol = Solution()
    print(sol.longestBalanced(nums))
