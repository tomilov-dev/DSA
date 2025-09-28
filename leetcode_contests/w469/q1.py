class Solution:
    def decimalRepresentation(self, n: int) -> list[int]:
        nums = []
        i = 1
        while n > 0:
            sub = n % (10**i)
            if sub != 0:
                nums.append(sub)
            n -= sub
            i += 1
        return list(reversed(nums))


if __name__ == "__main__":
    n = 102
    print(Solution().decimalRepresentation(n))
