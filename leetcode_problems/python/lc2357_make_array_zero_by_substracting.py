class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        uniq = set(nums)
        if len(uniq) == 1:
            if uniq.pop() == 0:
                return 0
            else:
                return 1

        steps = len(uniq)
        if 0 in uniq:
            steps -= 1

        return steps


if __name__ == "__main__":
    nums = [1, 5, 0, 3, 5]
    print(Solution().minimumOperations(nums))
