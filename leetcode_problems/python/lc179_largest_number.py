from functools import cmp_to_key


class Solution:
    def compare(self, x: str, y: str) -> int:
        if x + y > y + x:
            return -1
        elif x + y < y + x:
            return 1
        else:
            return 0

    def largestNumber(self, nums: list[int]) -> str:
        snums = [str(n) for n in nums]
        snums.sort(key=cmp_to_key(self.compare))
        result = "".join(snums)
        return result if result[0] != "0" else "0"


if __name__ == "__main__":
    nums = [3, 30, 34, 5, 9, 888]
    print(Solution().largestNumber(nums))
