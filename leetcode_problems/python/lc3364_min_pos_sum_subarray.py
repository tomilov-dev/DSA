class Solution:
    def minimumSumSubarray(
        self,
        nums: list[int],
        l: int,
        r: int,
    ) -> int:
        MAX = float("inf")
        mini = MAX

        for i in range(len(nums) - l + 1):
            xsum = sum(nums[i : i + l])
            if xsum > 0:
                mini = min(mini, xsum)

            for j in range(i + l, min(i + r, len(nums))):
                xsum += nums[j]
                if xsum > 0:
                    mini = min(mini, xsum)

        return mini if mini < MAX else -1


class SolutionSlidingWindow:
    def minimumSumSubarray(
        self,
        nums: list[int],
        l: int,
        r: int,
    ) -> int:
        MAX = float("inf")
        mini = MAX
        spr = r - l

        xsum = sum(nums[:l])
        lsum = xsum
        if xsum > 0:
            mini = min(mini, xsum)
        for i in range(l, r):
            lsum += nums[i]
            if lsum > 0:
                mini = min(mini, lsum)

        for i in range(l, len(nums)):
            xsum += nums[i] - nums[i - l]
            lsum = xsum
            if xsum > 0:
                mini = min(mini, xsum)

            for i in range(i + 1, min(i + spr + 1, len(nums))):
                lsum += nums[i]
                if lsum > 0:
                    mini = min(mini, lsum)

        return mini if mini < MAX else -1


if __name__ == "__main__":
    nums = [3, -2, 1, 4]
    l = 2
    r = 3
    print(Solution().minimumSumSubarray(nums, l, r))
    print(Solution2().minimumSumSubarray(nums, l, r))
