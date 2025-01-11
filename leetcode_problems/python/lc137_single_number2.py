class Solution:
    def singleNumber(
        self,
        nums: list[int],
    ) -> int:
        bits = [0] * 64
        for num in nums:
            num = num + 2**31
            i = 0
            while num:
                bits[i] += num % 2
                num //= 2
                i += 1

        num = 0
        for i in reversed(range(len(bits))):
            num = num * 2 + bits[i] % 3

        return num - 2**31


if __name__ == "__main__":
    nums = [2, 2, 3, 2]
    print(Solution().singleNumber(nums))
