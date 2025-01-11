class Solution:
    def threeSumClosest(
        self,
        nums: list[int],
        target: int,
    ) -> int:
        n = len(nums)
        res = float("inf")
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    loc = nums[i] + nums[j] + nums[k]
                    if abs(loc - target) < abs(res - target):
                        res = loc

        return res


class Solution2:
    def threeSumClosest(
        self,
        nums: list[int],
        target: int,
    ) -> int:
        n = len(nums)
        nums.sort()

        res = float("inf")
        for i in range(n):
            p1 = 0
            p2 = n - 1
            cur = 0
            while p1 < p2:
                if p1 == i:
                    p1 += 1
                    continue
                if p2 == i:
                    p2 -= 1
                    continue

                cur = nums[i] + nums[p1] + nums[p2]
                if abs(cur - target) < abs(res - target):
                    res = cur

                if cur > target:
                    p2 -= 1
                elif cur < target:
                    p1 += 1
                else:
                    return cur

        return res


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    print(Solution2().threeSumClosest(nums, target))
