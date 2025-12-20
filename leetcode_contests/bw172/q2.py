class SolutionBF:
    def maximumSum(self, nums: list[int]) -> int:
        n = len(nums)
        maxi = -1
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    sm = nums[i] + nums[j] + nums[k]
                    if sm % 3 == 0:
                        maxi = max(maxi, sm)
        return maxi


class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        mp: dict[int, list[int]] = dict()
        for num in nums:
            if num % 3 not in mp:
                mp[num % 3] = []
            mp[num % 3].append(num)

        allk = True
        for k in range(3):
            if k not in mp:
                allk = False
                continue
            mp[k] = mp[k][:3]

        maxi = 0
        if allk:
            maxi = max(maxi, mp[0][0] + mp[1][0] + mp[2][0])
        for k in range(3):
            if k in mp and len(mp[k]) >= 3:
                maxi = max(maxi, sum(mp[k]))
        return maxi


if __name__ == "__main__":
    nums = [4, 2, 3, 1]
    # nums = [2, 1, 5]
    print(Solution().maximumSum(nums))
