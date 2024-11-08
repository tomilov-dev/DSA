class Solution:
    def findLengthOfLCIS(
        self,
        nums: list[int],
    ) -> int:
        if len(nums) == 0:
            return 0

        subs = set([1])
        prev = float("-inf")
        sub = 0
        for num in nums:
            if num > prev:
                sub += 1
                prev = num
            else:
                subs.add(sub)
                sub = 1
                prev = num
        else:
            subs.add(sub)
        return max(subs)


class Solution2:
    def findLengthOfLCIS(
        self,
        nums: list[int],
    ) -> int:
        curl = 0
        maxl = 0
        prev = float("-inf")
        for num in nums:
            if num > prev:
                curl += 1
            else:
                curl = 1
            maxl = max(maxl, curl)
            prev = num

        return maxl


if __name__ == "__main__":
    nums = [1, 3, 5, 4, 7]
    nums = [2, 2, 2, 2, 2]
    nums = [1, 3, 5, 7]
    nums = [1, 3, 5, 4, 2, 3, 4, 5]
    print(Solution().findLengthOfLCIS(nums))
