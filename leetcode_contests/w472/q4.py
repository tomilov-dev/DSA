class Solution:
    def longestBalanced(self, nums: list[int]) -> int:
        n = len(nums)
        even = set()
        odd = set()
        pref = [(0, 0)]
        for num in nums:
            if num % 2 == 0:
                even.add(num)
            else:
                odd.add(num)
            pref.append((len(even), len(odd)))

        print(pref)
        diff_map = dict()
        longest = 0
        for i in range(n + 1):
            even, odd = pref[i]
            diff = even - odd
            if diff in diff_map:
                longest = max(longest, i - diff_map[diff])
            else:
                diff_map[diff] = i
        return longest


if __name__ == "__main__":
    nums = [2, 5, 4, 3]
    # nums = [3, 2, 2, 5, 4]
    # nums = [1, 2, 3, 2]1
    sol = Solution()
    print(sol.longestBalanced(nums))
