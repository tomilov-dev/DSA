class Solution:
    def split(self, num: int) -> list[int]:
        nums = []
        while num:
            nums.append(num % 10)
            num //= 10
        return nums

    def addDigits(self, num: int) -> int:
        while True:
            nums = self.split(num)
            if len(nums) < 2:
                return num
            num = sum(nums)


class Solution2:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9


if __name__ == "__main__":
    print(Solution().addDigits(0))
