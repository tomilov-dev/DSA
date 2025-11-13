class Solution:
    def maxKDistinct(self, nums: list[int], k: int) -> list[int]:
        nums.sort(reverse=True)
        res = []
        for i in range(len(nums)):
            if len(res) >= k:
                break
            if len(res) == 0:
                res.append(nums[i])
            elif nums[i - 1] == nums[i]:
                continue
            else:
                res.append(nums[i])
        return res


if __name__ == "__main__":
    nums = [84, 93, 100, 77, 90, 93]
    k = 3
    sol = Solution()
    res = sol.maxKDistinct(nums, k)
    print(res)
