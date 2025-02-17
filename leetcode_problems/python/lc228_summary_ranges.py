class Solution:
    def summaryRanges(
        self,
        nums: list[int],
    ) -> list[str]:
        p1 = 0
        p2 = 0

        ans = []
        while p2 < len(nums):
            while p2 + 1 < len(nums) and nums[p2 + 1] == nums[p2] + 1:
                p2 += 1

            if p1 == p2:
                ans.append(f"{nums[p1]}")
            else:
                ans.append(f"{nums[p1]}->{nums[p2]}")

            p2 += 1
            p1 = p2

        return ans


class Solution2:
    def summaryRanges(
        self,
        nums: list[int],
    ) -> list[str]:
        p1 = 0
        p2 = 0
        res = []
        while p1 < len(nums):
            while p2 + 1 < len(nums) and nums[p2] + 1 == nums[p2 + 1]:
                p2 += 1

            if p1 == p2:
                res.append(f"{nums[p1]}")
            else:
                res.append(f"{nums[p1]}->{nums[p2]}")

            p2 += 1
            p1 = p2

        return res


if __name__ == "__main__":
    nums = [0, 1, 2, 4, 5, 7]
    print(Solution2().summaryRanges(nums))
